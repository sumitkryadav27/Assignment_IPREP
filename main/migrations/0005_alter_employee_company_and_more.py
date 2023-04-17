# Generated by Django 4.1.4 on 2023-04-17 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_employee_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.company'),
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('id', 'company')},
        ),
    ]
