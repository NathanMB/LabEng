from django.contrib import admin
from .models import Patient, Exam, Report

# Register your models here

admin.site.register(Patient)
admin.site.register(Exam)
admin.site.register(Report)
