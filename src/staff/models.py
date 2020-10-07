from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EmployeeManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('You must have email address!')
        if not password:
            raise ValueError('You must have password!')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Employee(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    POSITION = {
        (1, 'Junior'),
        (2, 'Middle'),
        (3, 'Senior'),
        (4, 'Lead'),
    }

    position = models.IntegerField(choices=POSITION, default=1)

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=64, unique=True)
    avatar = models.ImageField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = EmployeeManager()

    def __str__(self):
        return self.email


class Device(models.Model):
    CATEGORIES = {
        (1, 'Laptop'),
        (2, 'Headphones'),
        (3, 'PC'),
        (4, 'Teapot'),
    }
    name = models.CharField(max_length=50, default=None)
    category = models.IntegerField(choices=CATEGORIES, default=1)
    image = models.ImageField(null=True)
    current_user = models.ForeignKey(Employee, default=None, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
