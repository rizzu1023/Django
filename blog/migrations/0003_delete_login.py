# Generated by Django 2.1.3 on 2018-11-06 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]
