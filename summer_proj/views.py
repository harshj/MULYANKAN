from django.shortcuts import render

def home(request):
	return render (request, 'home' )

def student_info(request):
	return render(request, 'student_info')
