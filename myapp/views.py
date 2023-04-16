from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from myapp.models import User,Deposit,Withdraw,Packages,PackageOrder
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import date, datetime, timedelta


# Create your views here.
class LoginPage(TemplateView):
    template_name = "myapp/earningapp/auth-login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
class Signup(TemplateView):
    template_name= "myapp/earningapp/auth-register.html"
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        ref = request.POST.get('reffer')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            phone_no = phone,
            refferedby = ref,

            ) 
        user.set_password(password)
        user.save()
        print(username,first_name,last_name,email,phone,ref)
        print(password)
        return redirect('login')
    
class Dashboard(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "myapp/earningapp/index.html"
class DepositView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name= "myapp/earningapp/payment.html"
    def post(self, request, *args, **kwargs):
        number = request.POST.get('number')
        form_number = request.POST.get('form_number')
        trxid = request.POST.get('trxid')
        amount = request.POST.get('amount')
        Deposit.objects.create(
            user=request.user,
            number= number,
            trx_id = trxid,
            payment_method = form_number,
            date = timezone.now(),
            amount = amount,
            status = 'Pending'
            )
        print(number)
        print(form_number)
        return redirect('index')

class DepositHistory(LoginRequiredMixin,TemplateView):
    template_name=template_name= "myapp/earningapp/history.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dh']=Deposit.objects.filter(user__username=self.request.user)
        return context
    

class WithdrawView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name= "myapp/earningapp/paymentw.html"
    def post(self, request, *args, **kwargs):
        number = request.POST.get('number')
        form_number = request.POST.get('form_number')
    
        amount = request.POST.get('amount')
        Withdraw.objects.create(
            user=request.user,
            number= number,
            payment_method = form_number,
            date = timezone.now(),
            amount = amount,
            status = 'Pending'
            )
        print(number)
        print(form_number)
        return redirect('index')
class WithdrawHistory(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/historyw.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dh']=Withdraw.objects.filter(user__username="admin")
        return context
class TeamView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/team.html"
class ProfileView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/profile.html"
class PackageView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/packages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        packs=Packages.objects.all()
        purpack= PackageOrder.objects.filter(user__username=self.request.user)
        for pack in packs:
            print("package: ",pack)
            pack.status= "none"
            for pur in purpack:
                 print(pur.status)
                 if str(pack)==str(pur) and pur.status=="Activate":
                     pack.status = "active"
                     
   
        context['packs'] = packs
        
        return context
    def post(self, request, *args, **kwargs):
        package =request.POST.get('package')
        validity =request.POST.get('validity')
        print(validity)
        PackageOrder.objects.create(
            user=request.user,
            package = Packages.objects.get(id=int(package)),
            purchase_date = date.today(),
            expire_date= date.today() + timedelta(days=int(validity)),
            status='Activate'
            
            )
        return redirect('package')

def logout_view(request):
    logout(request)
    return redirect('login')
