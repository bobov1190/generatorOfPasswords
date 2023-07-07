from django.urls import path
from generator_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('passwordGenerated', views.pwd, name='password'),
    path('aboutMe', views.about, name='aboutMe'),
]
