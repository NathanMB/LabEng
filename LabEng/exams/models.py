from django.db import models
from django.contrib.auth import get_user_model


class Patient(models.Model):
    SEX_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino')
    ]
    ETHINICITY_CHOICES = [
        ('Preto', 'Preto'),
        ('Branco', 'Branco'),
        ('Pardo', 'Pardo'),
        ('Indio', 'Inidio'),
        ('Amarelo', 'Amarelo')
    ]
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)
    ethinicity = models.CharField(max_length=10, choices=ETHINICITY_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('Ecocardiograma', 'Ecorcardiograma'),
        ('Electrocardiograma', 'Electrocardiograma'),
        ('Mapa', 'Mapa'),
        ('Holter', 'Holter')
    ]
    doctor = models.ForeignKey(get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', blank=False, null=False,on_delete=models.CASCADE)
    appointment_date = models.DateField(null=False)
    recommendations = models.CharField(max_length=300)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, blank=False, null=False)


class Report(models.Model):
    exam = models.ForeignKey('Exam', blank=False, null=False, on_delete=models.CASCADE)
    #resident = models.ForeignKey('Resident', blank=False, null=False, on_delete=models.CASCADE)
    approved = models.BooleanField()
    realization_date = models.DateField(null=False)
    diagnostic = models.CharField(max_length=300)

    """def get_upload_handler(instance, filename):
        return os.path.join('nomemedico', 'reports', 'nomearquivo')
    file = models.ImageField(null=False)"""
