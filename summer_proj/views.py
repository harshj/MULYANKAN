from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from summer_proj.forms import (
							result_eval_form , 
							centre_alloc_upload_form,
							re_evaluate_form,
							roll_search_form,
							)
							
from system.handle_uploads import (
								handle_response , 
								handle_key,
								handle_centre_info ,
								handle_student_info ,
								)
 
import system.centre_info
import system.roll_no_info
import system.centre_allocator
import system.result_evaluator
from system.constants import SYS_ROOT

import os


def home(request):
    return render( request , 'home' )

def roll_no_info(request):
    data,success,errors = system.roll_no_info.show()
    
    return render(request , 'roll_no_info' , {'data':data , 'success':success , 'errors':errors})

def centre_alloc(request):
	errors = []
	if request.method == 'POST' :
		upload_form = centre_alloc_upload_form(request.POST, request.FILES)

        # If file is uploaded.
		if upload_form.is_valid() :
        #	return HttpResponse("In Upload.")
			errors = handle_student_info(request.FILES['student_info'])				
			error = handle_centre_info(request.FILES['centre_info'])
			#return HttpResponse("upload handled." + error[0])
			for e in error:
				errors.append(e)
				
			if len(errors) == 0:
				upload_success = True
				success = system.centre_allocator.allocate()
				
				if(success):
					return HttpResponseRedirect('/roll_no_info/')
				else:
					return HttpResponse("Errors occurred while allocating centres. Please contact the admin")
			
			else:
				return HttpResponse("%d errors occurred while uploading. Please fix these errors\n 1. %s" , len(errors) , errors[0])
		
	else:
		upload_form = centre_alloc_upload_form()
	
	return render( request , 'centre_alloc' , 
    				{
    				 'upload_form' : upload_form,   
    				 'errors' : errors
    				 }
    			)

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
					if error[0][0] == "1":
						errors.append(error[0])
						return render(request, 'result_evaluator' , {'form' : form , 'errors' : errors})
					else:
						return HttpResponse("%d error has occurred while evaluation. Please Contact the site admin!!!" %len(error))
					
				else:
					# redirect to display result page
					return HttpResponseRedirect("/show_result/")
    
    else:
        form = result_eval_form()   
    return render(request, 'result_evaluator' , {'form' : form })

	
def show_result(request):
    data , success , errors = system.result_evaluator.show(0)   # 0 = sheet no. in result.xls
    return render(request, 'show_result' , {'data' : data ,'success' : success ,'errors' : errors})

# View to re-evaluate result.
def re_evaluate(request):
	if request.method == 'POST':
		form = re_evaluate_form(request.POST)
		if form.is_valid():
			questions = request.POST['questions']
			no_of_questions = request.POST['number_of_questions']
			
			if no_of_questions != '' :
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
	
def download(request, fname = ""):
	path = SYS_ROOT + os.sep + 'system' + os.sep + 'data' + os.sep
	
	if fname == 'result':
		fname = "Result.xls"
	elif fname == 'centre':
		fname = "Roll Number Information.xls"
	else:
		return HttpResponse("Invalid File Requested !!!")
	
	if os.path.exists(path + fname):
		f = open(path + fname , 'rb')
	else:
		return HttpResponse("404: File not found")
	
	xls = f.read()
	response = HttpResponse(xls , mimetype='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="%s"' %fname
	return response
	
# View to search allotted roll no. and centre information via application number.
def roll_search(request):

	info = []
	if request.method == 'POST':
		form = roll_search_form(request.POST)
		
		if form.is_valid():
			#return HttpResponse("Success")
			app_no = request.POST['application_no']
			errors, info = system.centre_info.get_centre(app_no)
			#return HttpResponse(info)
			if len(errors) > 0:
				return HttpResponse("%d errors have occurred. Please contact the site admin.", len(errors))
			else:
				return render(request , 'roll_search' , {'form' : form, 'info': info} )	
			
	form = roll_search_form
	return render(request , 'roll_search' , {'form' : form} )
