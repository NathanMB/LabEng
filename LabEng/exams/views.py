from django.shortcuts import render, redirect
from .forms import PatientForm, ExamForm

# Create your views here.

def registerPatient(request):
    form = PatientForm(request.POST)
    args = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('listPatients')

    return render(request, 'registrar_paciente.html', args)

def registerExam(request):
    form = ExamForm(request.POST)
    args = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('listExams')

    return render(request, 'registrar_exame.html', args)


def listPatients(request):
    return render(request, 'listar_pacientes.html')

def listExams(request):
    return render(request, 'listar_exames.html')