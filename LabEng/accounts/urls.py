from django.urls import path
from .views import login_user, exit_user, editar_perfil

urlpatterns = [
    path('', login_user, name='login_user'),
    path('logout', exit_user, name='exit_user'),
    path('editar-perfil', editar_perfil, name='editar_perfil')
]