"""generator_password URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from generator.views import home, password, user_data, form_save, dell_password
from registration.views import RegisterUser, LoginUser, logout_user
from django.conf import settings
from django.conf.urls.static import static

# from generator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('password/', password, name='password'),
    path('guest/', user_data, name='guest'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('save/', form_save, name='save'),
    path('delete/', dell_password, name='delete')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
