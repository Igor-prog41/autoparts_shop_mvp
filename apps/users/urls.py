from django.urls import path
from apps.users import  views
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", views.register_view_http, name="register"),
    path("login/", views.login_view_http, name="login"),
    path("logout/", views.login_view_http, name="logout"),
    path("profile/", views.login_view_http, name="profile"),

    path("api/register/", RegisterView.as_view(), name="api_register"),
    path("api/login/", TokenObtainPairView.as_view(), name="api_login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="api_token_refresh"),
]