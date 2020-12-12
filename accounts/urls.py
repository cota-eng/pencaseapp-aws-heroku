from django.urls import path
from .views import IndexView,ProfileView,ProfileEditView,LoginView,LogoutView,SignupView
app_name = "accounts"
urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit", ProfileEditView.as_view(), name="profile_edit"),
    path("login/", LoginView.as_view(), name="account_login"),
    path("logout/", LogoutView.as_view(), name="account_logout"),
    path("signup/", SignupView.as_view(), name="account_signup"),
]
