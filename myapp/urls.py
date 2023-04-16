from django.urls import path
from . import views

urlpatterns = [
path("", views.Dashboard.as_view(),name="index"),
path("login", views.LoginPage.as_view(),name="login"),
path("signup", views.Signup.as_view(),name="signup"),
path("deposit", views.DepositView.as_view(),name="deposit"),
path("deposit-history", views.DepositHistory.as_view(),name="deposit-history"),
path("withdraw", views.WithdrawView.as_view(),name="withdraw"),
path("withdraw-history", views.WithdrawHistory.as_view(),name="withdraw-history"),
path("team", views.TeamView.as_view(),name="team"),
path("profile", views.ProfileView.as_view(),name="profile"),
path("package", views.PackageView.as_view(),name="package"),
path('logout/', views.logout_view, name='logout'),
]