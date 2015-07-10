from django import forms
from django.core.validators import RegexValidator


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
										help_text = "<div class = 'help_text' >* Not Neccessary. Default value will be used. </div>",
										widget = forms.NumberInput(attrs=          
	                                                {'class':'text_input',
	                                                }
	                                                )
										)
	
class centre_alloc_upload_form(forms.Form):
	student_info = forms.FileField(label = "Student Information spreadsheet " , 
									help_text = "<div class = 'help_text' >(.xls) file </div>"
								)
	centre_info = forms.FileField(label = "Centre Information spreadsheet  " , help_text = "<div class = 'help_text' >(.xls) file </div>")
	

class re_evaluate_form(forms.Form):
	number_of_questions = forms.CharField(
	                                    label = "Number of Questions to be Evaluated",
	                                    required = False ,
	                                    help_text = "<div class = 'help_text'>* Not Neccessary. Default value will be used. </div>" ,
										widget = forms.TextInput( attrs = 
										                         { 
										                            'class':'text_input',
										                          }
										                          )
								        )
										
	questions = forms.CharField(
	                            label = " Questions to Uncheck" ,
	                            required = False ,
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
