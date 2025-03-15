from django.contrib.auth import views as auth_views
from django.urls import path
from .views import signup
from .views import account_view
from .views import get_attributes


urlpatterns = [
    path("home/", signup, name="signup"),
    path("signup/", signup, name="signup"),
    path("account/", account_view, name="account"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("attributes/", get_attributes, name="attributes"),
    # path("delete/", delete_account, name="delete_account"),
]


