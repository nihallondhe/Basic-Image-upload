from django import forms
from .models import Imageupload

class ImageForm(forms.ModelForm):
	class Meta:
		model = Imageupload
		fields  = '__all__'
		labels = {'img' : ''}