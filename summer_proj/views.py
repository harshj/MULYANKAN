from django.shortcuts import render
from django.http import HttpResponse
from forms import Student_Info_Form
from system.save_application import save
import os

def home(request):
	return render (request, 'home' )

def student_info(request):
	success = False	
	errors = []
	if request.method == 'POST':
		form = Student_Info_Form(request.POST)
		if form.is_valid():
			name = request.POST['name']
			fname = request.POST['fname']
			mname = request.POST['mname']
			address = request.POST['address']
			contact = request.POST['contact']
			flag,error =  save(name,fname,mname,address,contact)
			if flag == True :
				if len(error) == 0:
					success=True
					form = Student_Info_Form
				else:
					return HttpResponse("%d errors occured" %len(error))
				
			else:
				form = Student_Info_Form(request.POST)

			for e in error:
				errors.append(e)
	else:
		form = Student_Info_Form
	return render(request, 'student_info' , {'form':form , 'success':success , 'errors':errors})

def centre_info(request):
	return HttpResponse("This page is under development")


