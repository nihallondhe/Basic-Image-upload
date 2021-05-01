from django.shortcuts import render
from .forms import ImageForm
from .models import Imageupload
def home(request):
	if request.method == 'POST':
		form = ImageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	form = ImageForm
	imm = Imageupload.objects.all()
	return render (request,'home.html' , {'imm':imm,'forms':form})


