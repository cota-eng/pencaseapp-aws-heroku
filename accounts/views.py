from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import CustomUser
from django.views import View
from .forms import ProfileForm,SignupCustomForm
from allauth.account import views
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = "accounts/index.html"
    redirect_field_name = 'accounts:home'
    login_url = 'accounts:account_login'

class ProfileView(LoginRequiredMixin,View):
    redirect_field_name = 'accounts:home'
    login_url = 'accounts:account_login'
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        context = {
            "user_data":user_data
        }
        return render(request, "accounts/profile.html", context)
    
class ProfileEditView(LoginRequiredMixin,View):
    login_url = 'accounts:account_login'
    redirect_field_name = 'accounts:home'
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        context = {
            "user_data":user_data
        }
        form = ProfileForm(
            request.POST or None,
            initial={
                "ニックネーム":user_data.nickname
            }
        )
        return render(request, "accounts/profile_edit.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.nickname = form.cleaned_data["nickname"]
            user_data.save()
            return redirect('accounts:profile')
        return render(request, "accounts/profile.html", {'form':form})

class LoginView(views.LoginView):
    template_name = "account/login.html"
    success_url = "home"

class LogoutView(views.LogoutView):
    template_name = "account/logout.html"
    success_url = "home"

class SignupView(views.SignupView):
    template_name = "account/signup.html"
    form_class = "SignupCustomForm"
    success_url = "accounts:profile"