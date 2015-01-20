from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import Student_Info_Form

def home(request):
	return render (request, 'home' )

def student_info(request):
	form = Student_Info_Form()
	return render(request, 'student_info' , {'form':form})

def get_student_info(request):
	if request.method == 'POST':
		form = Student_Info_Form(request.POST)
		if form.is_valid():
			return render(request , 'student_info' , {'success' :True})
	else:
		form = Student_Info_Form()
	
	return render(request , 'student_info' , {'form' : form})
