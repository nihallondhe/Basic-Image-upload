from django.contrib import admin
from .models import Imageupload



@admin.register(Imageupload)
class ImageAdmin(admin.ModelAdmin):
	list_display = ['id' , 'img', 'date']



# Register your models here.
