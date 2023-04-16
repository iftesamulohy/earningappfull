from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import date

from myapp.models import Deposit, User,Withdraw,PackageOrder

@receiver(post_save, sender=Deposit)
def update_balance(sender, instance, **kwargs):
    if instance.status == 'Complete':
        balance = User.objects.get(username=instance.user.username)
        print(balance)
        balance.balance += instance.amount
        balance.save()

@receiver(post_save, sender=Withdraw)
def update_balance(sender, instance, **kwargs):
    if instance.status == 'Complete':
        balance = User.objects.get(username=instance.user.username)
        print(balance)
        balance.balance -= instance.amount
        balance.save()

@receiver(post_save, sender=PackageOrder)
def update_field_after_date(sender, instance, **kwargs):
    if date.today() > date(2022, 1, 1):
        print("expire date")
        instance.status= 'Expired'
        instance.save()