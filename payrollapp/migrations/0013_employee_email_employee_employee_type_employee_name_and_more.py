# Generated by Django 4.2.7 on 2023-11-18 21:19

from django.db import migrations, models
import payrollapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0012_auto_20231119_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_type',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Contractor', 'Contractor')], default='Employee', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.CharField(choices=[('State01', 'State01'), ('State02', 'State02')], max_length=20),
        ),
        migrations.AlterField(
            model_name='step1sub3',
            name='pincode',
            field=models.CharField(default='', max_length=10, validators=[payrollapp.models.validate_pincode]),
        ),
    ]