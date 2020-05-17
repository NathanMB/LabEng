from django.shortcuts import render, redirect
from .forms import PatientForm, ExamForm
from .models import Patient, Exam
from datetime import datetime, date
from django.core.exceptions import ObjectDoesNotExist

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


    if request.method == 'POST':
        exam = form.save(commit=False)
        exam.doctor = request.user
        try:
            cpf = request.POST["cpf_patient"]
            patient = Patient.objects.get(cpf=cpf)
            exam.patient = patient

            if form.is_valid():
                form.save()
                return redirect('listExams')
            else:
                return redirect('home')
        except ObjectDoesNotExist:
            return render(request, 'registrar_exame.html', args)

    elif request.method == 'GET':
        if "buscarPaciente" in request.GET:
            buscarPacientes = request.GET["buscarPaciente"]
            patients_list = Patient.objects.filter(first_name__icontains=buscarPacientes)
            args['patients_list'] = patients_list
            return render(request, 'registrar_exame.html', args)
        elif "cpfPaciente" in request.GET:
            return render(request, 'registrar_exame.html', args)

        return render(request, 'registrar_exame.html', args)



def listPatients(request):
    today = str(date.today())
    today = datetime.strptime(today, "%Y-%m-%d")

    patients = Patient.objects.all()

    for patient in patients:
        birth_date = str(patient.birth_date)
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

        age = int(((today - birth_date).days)/365)
        patient.age = age

    args = {'patients': patients}
    return render(request, 'listar_pacientes.html', args)

def listPatientsId(request, id):
    patient = Patient.objects.get(id=id)
    args = {"patient": patient}
    return render(request, "editar_paciente.html", args)

def listExams(request):
    exams = Exam.objects.all().filter(doctor=request.user)
    args = {'exams': exams}

    return render(request, 'listar_exames.html', args)

def listExamsId(request, id):
    exam = Exam.objects.get(id=id)
    args = {"exam": exam}
    return render(request, "editar_exame.html", args)


def listLaudos(request):
    args = {}
    return render(request, 'listar_laudo.html', args)