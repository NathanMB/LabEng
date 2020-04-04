from django.shortcuts import render, redirect

# Create your views here.

def registerPatient(request):

    return render(request, 'registrar_paciente.html')

def registerExam(request):
    return render(request, 'registrar_exame.html')