from django.urls import path
from .views import home, loginhandle, signup, logout_handle

app_name = 'authenticate'

urlpatterns = [
    path('', home, name='home'),
    path('login', loginhandle, name='loginhandle'),
    path('signup', signup, name='signup'),
    path('logout', logout_handle, name='logouthandle'),
]