from django import forms
from django.core.validators import RegexValidator

from system import constants


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
	
	def clean_response(self):
		res = self.cleaned_data['response']
		if res != None:
			response = str(res)
			extension = response.split('.')
			extension = extension[len(extension)-1]
			if extension != 'txt':
				raise forms.ValidationError(
											('Upload a valid .txt file : %(value)s'),
											params = {'value':res},
											)
		
		return res
		
	def clean_key(self):
		k = self.cleaned_data['key']
		if k != None:
			key = str(k)
			extension = key.split('.')
			extension = extension[len(extension)-1]
			if extension != 'txt':
				raise forms.ValidationError(
											('Upload a valid .txt file : %(value)s'),
											params = {'value':k},
											)
		return k
	
class centre_alloc_upload_form(forms.Form):
	student_info = forms.FileField(label = "Student Information spreadsheet " , 
									help_text = "<div class = 'help_text' >(.xls) file </div>"
								)
	centre_info = forms.FileField(label = "Centre Information spreadsheet  " , help_text = "<div class = 'help_text' >(.xls) file </div>")
	
	def clean_student_info(self):
		stud = self.cleaned_data['student_info']
		if stud != None:
			student_info = str(stud)
			extension = student_info.split('.')
			extension = extension[len(extension)-1]
			if extension != 'xls':
				raise forms.ValidationError(
											('Upload a valid .xls file : %(value)s'),
											params = {'value':stud},
											)
		
		return stud
		
	def clean_centre_info(self):
		centre = self.cleaned_data['centre_info']
		if centre != None:
			centre_info = str(centre)
			extension = centre_info.split('.')
			extension = extension[len(extension)-1]
			if extension != 'xls':
				raise forms.ValidationError(
											('Upload a valid .xls file : %(value)s'),
											params = {'value':centre},
											)
		
		return centre
	

class re_evaluate_form(forms.Form):
	number_of_questions = forms.IntegerField(
	                                    label = "Number of Questions to be Evaluated",
	                                    required = False ,
										max_value = constants.NO_OF_QUES,
										min_value = 1,
	                                    help_text = "<div class = 'help_text'>* Not Neccessary. Default value will be used. </div>" ,
										widget = forms.NumberInput( attrs = 
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
		
class roll_search_form(forms.Form):
	application_no = forms.IntegerField(
										label = "Application Number",
										min_value = 100000,
										max_value = 999999,
										required = True,
										help_text = "<div class = 'help_text'>* Your 6 digit application number.</div>" ,
										widget = forms.NumberInput(
																	attrs = {
																				'class': 'text_input', 
																				}
																)
										
									)