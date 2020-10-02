from django.db import models


class Model_1(models.Model):
    id = models.IntegerField(primary_key=True)
    field_1 = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}; {self.field_1}'
