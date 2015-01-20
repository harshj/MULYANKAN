from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import Student_Info_Form

def home(request):
	return render (request, 'home' )

def student_info(request):

	success = False	
	if request.method == 'POST':
		form = Student_Info_Form(request.POST)
		if form.is_valid():
			success=True
			form = Student_Info_Form()
	else:
		form = Student_Info_Form
	return render(request, 'student_info' , {'form':form , 'success':success})


