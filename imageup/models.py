from django.db import models


class Imageupload(models.Model):
	img = models.ImageField(upload_to = 'myimages/')
	date = models.DateTimeField(auto_now_add = True)
