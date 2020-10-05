from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from django.utils import timezone
# from .managers import EmployeeManager


# class Employee(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     name = models.CharField(max_length=255)
#     date_joined = models.DateTimeField(default=timezone.now)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = EmployeeManager()
#
#     def __str__(self):
#         return self.email
#
# class Employee(models.Model):
#     email
