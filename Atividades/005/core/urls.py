from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Index, name='Index'),
    path('login/', views.Login, name='Login'),
]
