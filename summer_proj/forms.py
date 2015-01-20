from django import forms

class Student_Info_Form(forms.Form):
	name = forms.CharField(max_length = 20)
	fname = forms.CharField(label = "Father's Name" ,max_length = 20)
	mname = forms.CharField(label = "Mother's Name" , max_length = 20)
	address = forms.CharField(max_length = 50)
	contact = forms.CharField(max_length = 10)

	def clean_contact(self):
		contact = self.cleaned_data['contact']
		number = 0
		count = 0

		if(len(contact) != 10):
                	raise forms.ValidationError("Invalid Number.Should be 10 digits long!!!")

		for i in contact:
			if(i.isdigit()):
				count = count + 1
				i = int(i)
				number = number * 10
				number = number + i	
			else:
				raise forms.ValidationError("Invalid Number.Only numbers are allowed!!!")

		return number
