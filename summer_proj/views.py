from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from summer_proj.forms import (
							student_info_form , 
							centre_info_form , 
							result_eval_form , 
							student_info_upload_form , 
							centre_info_upload_form ,
							re_evaluate_form
							)
							
from system.handle_uploads import (
								handle_response , 
								handle_key,
								handle_centre_info ,
								handle_student_info
								)

import system.student_application 
import system.centre_info
import system.roll_no_info
import system.centre_allocator
import system.result_evaluator

#import os


def home(request):
    return render( request , 'home' )

def student_info(request):
    success = False
    upload_success = False
    if request.method == 'POST':
        form = student_info_form(request.POST)
        upload_form = student_info_upload_form(request.POST, request.FILES)
        
        #If data is entered.
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
                
		# If file is uploaded.
       	elif upload_form.is_valid() :
        	#return HttpResponse("In Upload.")
			error = handle_student_info(request.FILES['student_info'])
			#return HttpResponse("upload handled." + error[0])
			if len(error) == 0:
				upload_success = True

    else:
        form = student_info_form
        upload_form = student_info_upload_form()
    return render(request, 'student_info' , 
    				{'form':form , 
    				'upload_form' : upload_form , 
    				'success':success , 
    				'upload_success' : upload_success}
    				)

def centre_info(request):
    success = False
    upload_success = False
    if request.method == 'POST' :
        form = centre_info_form(request.POST)
        upload_form = centre_info_upload_form(request.POST, request.FILES)

		# If data is entered.
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
					
		# If file is uploaded.
        elif upload_form.is_valid() :
        #	return HttpResponse("In Upload.")
			error = handle_centre_info(request.FILES['centre_info'])
			#return HttpResponse("upload handled." + error[0])
			if len(error) == 0:
				upload_success = True
		
    else:
        form = centre_info_form()
        upload_form = centre_info_upload_form()
    return render( request , 'centre_info' , 
    				{'form':form ,
    				 'upload_form' : upload_form, 
    				 'success':success , 
    				 'upload_success' : upload_success} 
    				 )

def roll_no_info(request):
    data,success,errors = system.roll_no_info.show()
    
    return render(request , 'roll_no_info' , {'data':data , 'success':success , 'errors':errors})

def centre_alloc(request):
	success = system.centre_allocator.allocate()
	return HttpResponseRedirect('/roll_no_info/')
	#return render( request, 'roll_no_info' , {'alloc_success' : success} )

def result_evaluator(request):
    errors = []
    success = False
    if request.method == "POST":
	
            form = result_eval_form(request.POST,request.FILES)
            if form.is_valid():
				# handle uploaded files
				error = handle_response(request.FILES['response'])
				if len(error) != 0:
					return HttpResponse(" %d An error has occured with response file. Contact admin!!!" %len(error) + error[0])
				
				if 'key' in request.FILES.iterkeys() :		# Check if key.txt was uploaded
					error = handle_key(request.FILES['key'])
					if len(error) != 0:
						return HttpResponse("An error has occured with key file. Contact admin!!!")
				
				no_of_questions = request.POST['no_of_questions']
				if no_of_questions != '':
					no_of_questions = int( no_of_questions )
					# call result generation module
					error = system.result_evaluator.evaluate("" , no_of_questions)
				else:
					error = system.result_evaluator.evaluate()
				
				if len(error) != 0 :
					return HttpResponse("%d error has occurred while evaluation. Please Contact the site admin!!!" %len(error))
					
				else:
					# redirect to display result page
					return HttpResponseRedirect("/show_result/")
    
    else:
        form = result_eval_form()   
    return render(request, 'result_evaluator' , {'form' : form , 'errors' : errors})

	
def show_result(request):
    data , success , errors = system.result_evaluator.show(0)
    return render(request, 'show_result' , {'data' : data ,'success' : success ,'errors' : errors})

# View to re-evaluate result.
def re_evaluate(request):
	if request.method == 'POST':
		form = re_evaluate_form(request.POST)
		if form.is_valid():
			questions = request.POST['questions']
			no_of_questions = request.POST['no_of_questions']
			if no_of_questions != '':
				no_of_questions = int( no_of_questions )
				error = system.result_evaluator.evaluate(questions , no_of_questions)
			else:
				error = system.result_evaluator.evaluate(questions)
				
			if len(error) != 0 :
					return HttpResponse("An error has occurred while evaluation. Please Contact the site admin!!! ")
					
			else :
				# redirect to display result page
				return HttpResponseRedirect("/show_result/")
					

   	else:
		form = re_evaluate_form()
	return render(request,'re_evaluate' , {'form' : form})
	
# View to show question wise result analysis.
def analysis(request):
	data , success , errors = system.result_evaluator.show(1)
	return render(request, 'show_analysis' , {'data' : data ,'success' : success ,'errors' : errors})
	
