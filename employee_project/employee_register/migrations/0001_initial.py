# Generated by Django 2.2.4 on 2019-12-12 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('empCode', models.CharField(max_length=6)),
                ('mobileNo', models.CharField(max_length=10)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.Position')),
            ],
        ),
    ]
