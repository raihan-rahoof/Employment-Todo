# Generated by Django 5.1.2 on 2024-10-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('EMPLOYER', 'Employer'), ('EMPLOYEE', 'Employee'), ('ADMIN', 'Admin')], default='EMPLOYEE', max_length=10),
        ),
    ]
