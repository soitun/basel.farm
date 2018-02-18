"""basel_farm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework import routers
from app_main.views import StockViewSet, TransactionViewSet
from app_main import views

router = routers.SimpleRouter()
router.register(r'api/transaction', TransactionViewSet, 'Transaction')
router.register(r'api/stock', StockViewSet, 'Stock')

urlpatterns = [
    path('', RedirectView.as_view(url='/transactions')),
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('stocks/', views.stock_manager, name="stocks"),
    path('transactions/', views.transactions, name="transactions"),
]

urlpatterns += router.urls