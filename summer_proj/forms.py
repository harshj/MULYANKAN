from django import forms

class Student_Info_Form(forms.Form):
	name = forms.CharField(max_length = 20)
	fname = forms.CharField(max_length = 20)
	address = forms.CharField(max_length = 100)
	contact = forms.CharField(max_length = 15)
