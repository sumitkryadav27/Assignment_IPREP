# Generated by Django 4.1.4 on 2023-04-17 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_employee_company'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.company'),
        ),
    ]