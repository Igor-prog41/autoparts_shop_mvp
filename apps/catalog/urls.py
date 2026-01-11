from django.urls import path
from apps.catalog import  views

urlpatterns = [
    path('',views.catalog, name="catalog"),
    path('about/', views.about, name="about"),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
]