"""
URL configuration for telegramPanel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from monogram import views
from bot1.views import tst

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('bot', views.bot, name='bot'),
    path('bot', views.UpdateHandler, name='bot'),
    # path('bot', test.as_view(), name='bot'),
    path('bot1', tst, name='bot1'),
    # path("bot1", include('bot1.urls'))

]
