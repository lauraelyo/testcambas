# Generated by Django 2.1 on 2019-05-22 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
    ]
