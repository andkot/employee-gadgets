# Generated by Django 3.1.2 on 2020-10-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('score', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
