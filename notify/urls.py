from django.urls import path
from .views import notify_info

app_name = 'posts'

urlpatterns = [
    path('', notify_info, name='notify-info'),
]