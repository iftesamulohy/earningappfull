# Generated by Django 4.1.7 on 2023-04-15 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=15, null=True)),
                ('payment_method', models.CharField(blank=True, choices=[('bkash', 'Bkash'), ('nagad', 'Nagad')], max_length=10, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Complete', 'Completed'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
