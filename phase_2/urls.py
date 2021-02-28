"""phase_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from webpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #HOLD UP!!!
    # home function points to the function which is exactly similar to success function so just replace it with the home page.
    path('home/', views.home, name='webpages-home'),
    # 'register/' is searched and cutoff from the address if found and the remaining portion is sent to register.urls
    path('success/', views.success, name='success'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('challenges/',include('challenges.urls'))    
]


