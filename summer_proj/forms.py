from django import forms
from django.core.validators import RegexValidator

class student_info_form(forms.Form):
	name = forms.CharField(label = "Name \t " , max_length = 20)
	fname = forms.CharField(label = "Father's Name \t " ,max_length = 20)
	mname = forms.CharField(label = "Mother's Name \t " , max_length = 20)
	address = forms.CharField(label = "Address \t " , max_length = 50)
	contact = forms.CharField(label = "Contact \t " , max_length = 10)

	def clean_contact(self):
		contact = self.cleaned_data['contact']
		number = 0
		count = 0

		if(len(contact) != 10):
                	raise forms.ValidationError("Invalid Number.Should be 10 digits long!!!")

		if(contact.isdigit()):
			for i in contact:
				count = count + 1
				i = int(i)
				number = number * 10
				number = number + i	
		else:
			raise forms.ValidationError("Invalid Number.Only numbers[0-9] are allowed!!!")

		return number

class centre_info_form(forms.Form):
	cname = forms.CharField(label = "Centre Name " , max_length = 20)
	caddress = forms.CharField(label = "Centre Address " , max_length = 50)
	capacity = forms.CharField(label = "Capacity ")

	def clean_capacity(self):
		capacity = self.cleaned_data['capacity']
		if capacity.isdigit():
			if int(capacity) == 0:
				raise forms.ValidationError("Centre Capacity should be greater than zero")
		else:
			raise forms.ValidationError("Enter a valid number!!!")
		return capacity		


class result_eval_form(forms.Form):
	response = forms.FileField(label = "Response File", help_text = "(.txt) file")
	key = forms.FileField(label = "Key File" , required = False , help_text = '(.txt) file')
	
class student_info_upload_form(forms.Form):
	student_info = forms.FileField(label = "Student Information spreadsheet" , help_text = "(.xls) file")
	
class centre_info_upload_form(forms.Form):
	centre_info = forms.FileField(label = "Centre Information spreadsheet" , help_text = "(.xls) file")

class re_evaluate_form(forms.Form):
	questions = forms.CharField(
								label = "Questions to Uncheck \n\n" , 
								help_text = "Seperate multiple with blank spaces (' ') " , 
								)

	def clean_questions(self):
		questions = self.cleaned_data['questions']
		for qno in questions.split():
			if qno.isdigit() == False:
				raise forms.ValidationError("Invalid Number")
				break
		return questions
