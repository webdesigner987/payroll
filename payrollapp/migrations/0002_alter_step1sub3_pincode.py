# Generated by Django 4.2.7 on 2023-11-10 19:38

from django.db import migrations, models
import payrollapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step1sub3',
            name='pincode',
            field=models.CharField(default='', max_length=10, validators=[payrollapp.models.validate_pincode]),
        ),
    ]
