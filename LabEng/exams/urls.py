from django.urls import path
from .views import registerPatient, registerExam, listPatients, listExams, listLaudos, listPatientsId, listExamsId


urlpatterns = [
    path('cadastrar/paciente', registerPatient, name='registerPatient'),
    path('cadastrar/exame', registerExam, name='registerExam'),
    path('listar/pacientes', listPatients, name='listPatients'),
    path('listar/exames', listExams, name='listExams'),
    path('listar/laudos', listLaudos, name='listLaudos'),
    path('pacientes/<int:id>/editar', listPatientsId, name="listPatientsId"),
    path('exames/<int:id>/editar', listExamsId, name='listExamsId')


]