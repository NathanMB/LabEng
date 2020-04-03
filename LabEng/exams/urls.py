from django.urls import path
from .views import registerPatient, registerExam


urlpatterns = [
    path('cadastrar/paciente', registerPatient, name='registerPatient'),
    path('cadastrar/exame', registerExam, name='registerExam')
]