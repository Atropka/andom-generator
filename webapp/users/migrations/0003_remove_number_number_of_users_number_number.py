# Generated by Django 4.1.7 on 2023-02-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='number',
            name='number_of_users',
        ),
        migrations.AddField(
            model_name='number',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
