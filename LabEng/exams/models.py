from django.db import models


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


class Exams(models.Model):
    pass

class Reports(models.Model):
    pass