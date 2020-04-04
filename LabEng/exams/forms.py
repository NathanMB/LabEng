from django.forms import ModelForm
from django import forms

from .models import Patient, Exam

class PatientForm(ModelForm):

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'sex', 'ethinicity']


class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['patient', 'doctor', 'appointment_date', 'recommendations', 'exam_type']