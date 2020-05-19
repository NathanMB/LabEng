from django.urls import path
from .views import registerPatient, registerExam, listPatients, listExams, listLaudos, listPatientsId, listExamsId, registerReport, listReportId


urlpatterns = [
    path('cadastrar/paciente', registerPatient, name='registerPatient'),
    path('cadastrar/exame', registerExam, name='registerExam'),
    path('listar/pacientes', listPatients, name='listPatients'),
    path('listar/exames', listExams, name='listExams'),
    path('listar/laudos', listLaudos, name='listLaudos'),
    path('pacientes/<int:id>/editar', listPatientsId, name="listPatientsId"),
    path('exames/<int:id>/editar', listExamsId, name='listExamsId'),
    path('laudo/<int:id>/editar', listReportId, name="listReportId"),
    path('cadastrar/laudo', registerReport, name="registerReport")


]