# Generated by Django 3.0.1 on 2019-12-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
