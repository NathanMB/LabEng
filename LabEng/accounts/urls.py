from django.urls import path
from .views import login_user, exit_user

urlpatterns = [
    path('', login_user, name='login_user'),
    path('logout', exit_user, name='exit_user')
]