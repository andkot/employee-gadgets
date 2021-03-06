# Generated by Django 3.1.2 on 2020-10-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.IntegerField(choices=[(1, 'Laptop'), (4, 'Teapot'), (2, 'Headphones'), (3, 'PC')], default=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.IntegerField(choices=[(4, 'Lead'), (1, 'Junior'), (2, 'Middle'), (3, 'Senior')], default=1),
        ),
    ]
