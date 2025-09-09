from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products, name='list_products'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('search/<str:query>/', views.search_products, name='search_products'),
]