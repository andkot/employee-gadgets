# Generated by Django 3.1.2 on 2020-10-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_1',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
