from django.urls import path
from apps.users import  views_http
from .views_api import RegisterView, LoginView
from rest_framework_simplejwt.views import  TokenRefreshView


urlpatterns = [
    path("register/", views_http.register_view_http, name="register"),
    path("login/", views_http.login_view_http, name="login"),
    path("logout/", views_http.logout_view_http, name="logout"),
    path("profile/", views_http.profile_view_http, name="profile"),

    path("api/register/", RegisterView.as_view(), name="api_register"), # correct
    path("api/login/", LoginView.as_view(), name="api_login"),  # correct, change to custom
    path("api/refresh/", TokenRefreshView.as_view(), name="api_token_refresh"),  #correct
    path("api/logout/", views_http.logout_view_http, name="api_logout"),
    path("api/profile/", views_http.profile_view_http, name="api_profile"),
]