
from django.urls import path, include
from . import views

app_name= "challenges"
urlpatterns = [
    path('',views.home,name='home'),
    path('warmup',views.warmup,name='warmup'),
    path('robots',views.robots,name='robots'),
    #path('robots/robots.txt',views.read_file,name='robots_txt')
]