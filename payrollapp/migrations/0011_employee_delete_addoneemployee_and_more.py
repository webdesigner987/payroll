# Generated by Django 4.2.7 on 2023-11-18 20:59

from django.db import migrations, models
import payrollapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0010_addoneemployee_delete_addone_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hire_date', models.DateField()),
                ('job_title', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('manager', models.CharField(choices=[('emp01', 'emp01'), ('emp02', 'emp02')], max_length=10)),
                ('annual_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(choices=[('State01', 'State01'), ('State02', 'State02')], max_length=10)),
                ('resident_of_india', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='AddOneEmployee',
        ),
        migrations.AlterField(
            model_name='step1sub3',
            name='pincode',
            field=models.CharField(default='', max_length=10, validators=[payrollapp.models.validate_pincode]),
        ),
    ]