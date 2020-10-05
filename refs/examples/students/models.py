from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    score = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    def __str__(self):
        return f'{self.id}: {self.name}'
