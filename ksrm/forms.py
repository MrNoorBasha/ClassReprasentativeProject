from django import forms
from .models import Student1, Professor



class Studentform(forms.ModelForm):

	class Meta:
		
		model=Student1
		fields='__all__'
		# fields=['name','rollno','subjects']


class ProfessorForm(forms.ModelForm):
	class Meta:
		model = Professor
		fields = '__all__'


