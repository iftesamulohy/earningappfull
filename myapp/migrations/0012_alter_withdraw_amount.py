# Generated by Django 4.1.7 on 2023-04-15 06:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_withdraw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='amount',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
