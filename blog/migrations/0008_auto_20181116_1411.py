# Generated by Django 2.1.3 on 2018-11-16 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181116_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
