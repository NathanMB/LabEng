from django.urls import path
from .views import registerPatient, registerExam, listPatients, listExams, listReport, listPatientsId, listExamsId, registerReport, listReportId, performExam


urlpatterns = [
    path('paciente/cadastrar', registerPatient, name='registerPatient'),
    path('paciente/listar', listPatients, name='listPatients'),
    path('paciente/<int:id>/editar', listPatientsId, name="listPatientsId"),

    path('exame/cadastrar', registerExam, name='registerExam'),
    path('exame/listar', listExams, name='listExams'),
    path('exame/<int:id>/editar', listExamsId, name='listExamsId'),
    path('exame/<int:id>/realizar', performExam, name='performExam'),

    path('laudo/cadastrar', registerReport, name='registerReport'),
    path('laudo/listar', listReport, name='listReport'),
    path('laudo/<int:id>/editar', listReportId, name='listReportId'),


]