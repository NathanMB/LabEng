from django.db import models
from django.contrib.auth import get_user_model
from exams.choices import SEX_CHOICES, ETHINICITY_CHOICES, EXAM_TYPE_CHOICES
import os


class Patient(models.Model):
    cpf = models.CharField(max_length=14, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)
    birth_date = models.DateField(null=True)
    ethinicity = models.CharField(max_length=10, choices=ETHINICITY_CHOICES, blank=False, null=False)



    def __str__(self):
        return self.first_name + " " + self.last_name

class Exam(models.Model):
    doctor = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', blank=True, null=True,  on_delete=models.CASCADE)
    appointment_date = models.DateField(blank=False, null=False)
    recommendations = models.CharField(blank=False, null=False, max_length=300)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, blank=False, null=False)

    def __str__(self):
        return str(self.id)


class Report(models.Model):
    exam = models.ForeignKey('Exam', blank=False, null=False, on_delete=models.CASCADE)
    medico = models.ForeignKey('accounts.Medico', blank=False, null=True, on_delete=models.CASCADE)
    approved = models.BooleanField()
    realization_date = models.DateField(null=False)
    diagnostic = models.CharField(max_length=100)

    def get_upload_handler(instance, filename):
        email = instance.medico.email
        return os.path.join('static', 'medicos', email, 'reports', filename)
        #'D:\LabEng\LabEng\static\medicos\zika@gmail.com\reports\relatorio01.pdf'


    file = models.FileField(upload_to=get_upload_handler, null=True, blank=True)

    def __str__(self):
        return str(self.exam.id)