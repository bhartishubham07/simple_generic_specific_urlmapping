from pgproject.views import *
from django.urls import path

app_name = 'pgproject'

urlpatterns = [
    path('home/', home, name='home'),
    path('add/', add, name='add'),
    path('get/', get, name='get'),
    path('delete/', delete, name='delete'),
]
