from django.shortcuts import render,redirect
from .forms import Studentform, ProfessorForm
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from .models import Student1, Professor

# Create your views here.
...


def welcome(request):
	return render(request,'ksrm/hello.html',{})

def index(request):
		return render(request,'ksrm/index.html',{})

# Studet Records Functions
...
def student_submit(request):
	if request.method=='POST':
		data=Studentform(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("<h1>alert('Data save succesfull.</h1>")
		data=request.POST
		return HttpResponse('WELCOME TO'+ data['name'])
	stuform=Studentform()
	return render(request,'ksrm/student_submit.html',{'formfields':stuform})

def student_records(request):
	data=Student1.objects.all()
	return render(request,'ksrm/student_records.html',{'data':data})

def student_show(request,id):
	data=Student1.objects.get(id=id)
	return render(request,"ksrm/student_show.html" ,{'data':data})

def student_update(request,id):
	data = Student1.objects.get(id=id)
	form = Studentform(instance=data)
	if request.method=='POST':
		form = Studentform(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/Student_records')
	return render(request,'ksrm/student_update.html',{'form':form})

def student_delete(request,id):
	data=Student1.objects.get(id=id)
	if request.method == 'POST':
		data.delete()
		return redirect('/Student_records')
	return render(request,"ksrm/student_delete.html",{'data':data})


# Professor_details
...


def professor_submit(request):
	if request.method=='POST':

		data = ProfessorForm(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("<h1> Data save succesfully</h1>")
	
		data = request.POST
		return HttpResponse('WELCOME TO'+ data['name'])
	proform = ProfessorForm()
	return render(request, 'ksrm/professor_submit.html', {'formfields': proform})
	

def professor_records(request):
	data = Professor.objects.all()
	return render(request, 'ksrm/professor_records.html', {'data': data})

def professor_show(request,id):
	data=Professor.objects.get(id=id)
	return render(request,"ksrm/professor_show.html" ,{'data':data})

def professor_update(request,id):
	data = Professor.objects.get(id=id)
	form = ProfessorForm(instance=data)
	if request.method=='POST':
		form = ProfessorForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/Professor_records')
	return render(request,'ksrm/professor_update.html',{'form':form})

def professor_delete(request,id):
	data=Professor.objects.get(id=id)
	if request.method == 'POST':
		data.delete()
		return redirect('/Professor_records')
	return render(request,"ksrm/professor_delete.html",{'data':data})

