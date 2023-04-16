from django import forms
from django.conf import settings
from django.contrib import admin
from .models import Deposit, User, Withdraw,Packages,PackageOrder

# Register your models here.
from solo.admin import SingletonModelAdmin
from myapp.models import Aboutus, PrivacyPolicy, Terms
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.admin.models import LogEntry



class MyModelAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        models = [Aboutus,PrivacyPolicy, Terms]
        fields = '__all__'
class AboutusAdmin(SingletonModelAdmin):
    form = MyModelAdminForm
class PrivacyAdmin(SingletonModelAdmin):
    form = MyModelAdminForm
class TermsAdmin(SingletonModelAdmin):
    form = MyModelAdminForm
class DepositAdmin(admin.ModelAdmin):
    list_display = ['user','number','payment_method','status']
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['user','number','payment_method','status']
admin.site.register(Deposit,DepositAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Withdraw,WithdrawAdmin)
admin.site.register(Packages)
admin.site.register(PackageOrder)
admin.site.register(User)