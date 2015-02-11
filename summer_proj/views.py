from django.shortcuts import render,redirect
from django.http import HttpResponse
from summer_proj.forms import student_info_form,centre_info_form,result_eval_form
import system.student_application 
import system.centre_info
import system.roll_no_info
import system.centre_allocator
import system.result_evaluator
import os

def home(request):
	return render( request , 'home' )

def student_info(request):
	success = False	
	errors = []
	if request.method == 'POST':
		form = student_info_form(request.POST)
		if form.is_valid():
			name = request.POST['name']
			fname = request.POST['fname']
			mname = request.POST['mname']
			address = request.POST['address']
			contact = request.POST['contact']
			flag,error =  system.student_application.save(name,fname,mname,address,contact)
			if flag == True :
				if len(error) == 0:
					success=True
					form = student_info_form
				else:
					return HttpResponse("%d errors occured while saving.Please contact the site admin" %len(error))
				
			else:
				form = student_info_form(request.POST)

	else:
		form = student_info_form
	return render(request, 'student_info' , {'form':form , 'success':success , 'errors':errors})

def centre_info(request):
	success = False
	errors = []
	if request.method == 'POST' :
		form = centre_info_form(request.POST)
		if form.is_valid():
			cname = request.POST['cname']
			caddress = request.POST['caddress']
			capacity = request.POST['capacity']
			flag,error = system.centre_info.save(cname,caddress,capacity)
			if(flag == True):
				if(len(error) == 0):	
					success = True
				else:
					return HttpResponse("%d errors occurred while saving. Please contact the site admin" %len(error))
	else:
		form = centre_info_form
	return render(request , 'centre_info' , {'form':form , 'success':success , 'errors':errors}
)

def roll_no_info(request):
	data,success,errors = system.roll_no_info.show()
	
	return render(request , 'roll_no_info' , {'data':data , 'success':success , 'errors':errors})

def centre_alloc(request):
	success = system.centre_allocator.allocate()
	return render(request, 'home' , {'alloc_success':success})

def result_evaluator(request):
	'''errors = []
	success = False
	if request.method == "POST":
        	form = result_eval_form(request.POST,request.FILES)
		if form.is_valid():
		#	result_evaluator.save(request.FILES['response'])
			flag,error = system.result_evaluator.evaluate()
			if len(error) != 0 :
				return HttpResponse("An error has occurred. Please Contact the site admin!!!")
			if flag:
				return redirect('show_result')
	
	else:
		form = result_eval_form		
	return render(request, 'result_evaluator' , {'form' : form , 'success' : success , 'errors' : errors})'''

	success , errors = system.result_evaluator.evaluate()
	if len(errors) != 0:
		return HttpResponse("An error has occurres. Please contact the site admin!!!")
	return render(request,'home',{'eval_success':success})
	
def show_result(request):
	data , success , errors = system.result_evaluator.show()
	return render(request, 'show_result' , {'data' : data ,'success' : success ,'errors' : errors})
