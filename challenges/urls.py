from django.urls import path, include
from . import views

app_name= "challenges"
urlpatterns = [
    path('',views.home,name='challenges-home'),
    #path('robots/robots.txt',views.read_file,name='robots_txt')
]