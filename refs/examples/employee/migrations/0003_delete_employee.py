# Generated by Django 3.1.2 on 2020-10-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_is_staff'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
