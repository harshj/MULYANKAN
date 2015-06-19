from django import forms
from django.core.validators import RegexValidator

class student_info_form(forms.Form):
	name = forms.CharField(
	                        label = "Name \t " ,
	                        max_length = 20,
	                        widget = forms.TextInput(attrs = 
	                                                {
	                                                 'class' : 'text_input',
	                                                }
	                                                )
	                        )
	father_name = forms.CharField(
	                        label = "Father's Name \t " ,
	                        max_length = 20,
	                        widget = forms.TextInput(attrs = 
	                                                {
	                                                'class' : 'text_input',
	                                                }
	                                                )
	                        )
	mother_name = forms.CharField(
	                        label = "Mother's Name \t " , 
	                        max_length = 20,
	                        widget = forms.TextInput(attrs = 
	                                                 {
	                                                   'class' : 'text_input',
	                                                 }
	                                                 )
	                        )
	address = forms.CharField(
	                         label = "Address \t " , 
	                         max_length = 50,
	                        widget = forms.TextInput(attrs = 
	                                                {
	                                                'class':'text_input',
	                                                }
	                                                )
	                          )
	contact = forms.CharField(
	                         label = "Contact \t " , 
	                         max_length = 10,
	                        widget = forms.NumberInput(attrs = 
	                                                {
	                                                'class':'text_input',
	                                                }
	                                                )
	                          )

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
	center_name = forms.CharField(
	                        max_length = 20 ,
	                        widget = forms.TextInput(attrs=          
	                                                {'class':'text_input',
	                                                }
	                                                )
	                        )              
	center_address = forms.CharField(
	                         widget = forms.TextInput(attrs=          
	                                                {'class':'text_input',}
	                                                )
	                        )
	capacity = forms.CharField(widget = forms.NumberInput( attrs = { 'class':'text_input', } )
	                          )

	def clean_capacity(self):
		capacity = self.cleaned_data['capacity']
		if capacity.isdigit():
			if int(capacity) == 0:
				raise forms.ValidationError("Centre Capacity should be greater than zero")
		else:
			raise forms.ValidationError("Enter a valid number!!!")
		return capacity		


class result_eval_form(forms.Form):
	response = forms.FileField(
	                            label = "Response File", 
	                            help_text = "<div class = 'help_text' >* (.txt) file </div>"
	                           )
	                           
	key = forms.FileField(
	                        label = "Key File" , 
	                        required = False , 
	                        help_text = "<div class = 'help_text' >* (.txt) file </div>"
	                        )
	no_of_questions = forms.CharField(
										label = "Number of Questions to be Evaluated \n \n" ,
										required = False,
										help_text = "<div class = 'help_text' >* Not Neccessary </div>",
										widget = forms.NumberInput(attrs=          
	                                                {'class':'text_input',
	                                                }
	                                                )
										)
	
class student_info_upload_form(forms.Form):
	student_info = forms.FileField(label = "Student Information spreadsheet  " , help_text = "<div class = 'help_text' >(.xls) file </div>")
	
class centre_info_upload_form(forms.Form):
	centre_info = forms.FileField(label = "Centre Information spreadsheet  " , help_text = "<div class = 'help_text' >(.xls) file </div>")

class re_evaluate_form(forms.Form):
	number_of_questions = forms.CharField(
	                                    label = "Number of Questions to be Evaluated",
	                                    required = False ,
	                                    help_text = "<div class = 'help_text'>* Not Neccessary </div>" ,
										widget = forms.TextInput( attrs = 
										                         { 
										                            'class':'text_input',
										                          }
										                          )
								        )
										
	questions = forms.CharField(
	                            label = " Questions to Uncheck" ,
	                            help_text = "<div class = 'help_text'>* Seperate multiple with blank spaces (' ') </div>" , 
	                            widget = forms.TextInput( attrs =
								                         {
								                           'class' : 'text_input',
								                           }
								                           )
								 )


	def clean_questions(self):
		questions = self.cleaned_data['questions']
		for qno in questions.split():
			if qno.isdigit() == False:
				raise forms.ValidationError("Invalid Number")
				break
		return questions
