from django.forms import ModelForm
from django import forms
from exams.choices import *

from .models import Patient, Exam, Report

class PatientForm(ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'lname'
        }))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'llast-name'
        }))
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.Select(attrs={
            'id': 'inputGroupSelect01',
            'class': 'custom-select'
        }))

    ethinicity = forms.ChoiceField(
        choices=ETHINICITY_CHOICES,
        widget=forms.Select(attrs={
            'id': 'lethinicity',
        }))
    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'lcpf',
        }))

    birth_date = forms.DateField(
        widget=forms.DateInput()
    )




    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'sex', 'ethinicity', 'cpf', 'ethinicity', 'birth_date']


class ExamForm(ModelForm):
    """patient = forms.ModelChoiceField(
        queryset=Patient.objects.all().filter(cpf='0'),
        widget=forms.Select(attrs={'max-width': '100', 'required': 'false'}),
        empty_label='---------'
    )"""
    """patient = forms.CharField(
        widget=forms.TextInput(attrs={'size': '40', 'required:': 'false'})
    )"""

    appointment_date = forms.DateField(
        widget=forms.SelectDateWidget(attrs={})
    )
    recommendations = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={'cols': '50%'})
    )
    exam_type = forms.ChoiceField(
        choices=EXAM_TYPE_CHOICES,
        widget=forms.Select()
    )


    class Meta:
        model = Exam
        fields = ['patient','appointment_date', 'recommendations', 'exam_type']


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['exam', 'medico', 'approved', 'realization_date', 'diagnostic', 'file']