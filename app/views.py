from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files import File
from app.models import *
from UploadImages import settings
from uuid import uuid4
import requests, urllib.request
import os


def imagesList(request):	
	images = Image.objects.all()	
	return render(request, "images_list.html", {'images': images })

def addImage(request):		
	if request.method == "GET":        
		return render(request, "add_image.html")

	if (request.POST.get('image_link') and request.FILES) or (not request.POST.get('image_link') and not request.FILES):
		messages.error(request, "Введите либо ссылку, либо добавьте файл")
		return render(request, "add_image.html")	

	if request.POST.get('image_link'):		
		url = request.POST.get('image_link')		
		f_name = url.split('/')[-1]		
		abs_url = settings.MEDIA_ROOT + '\\' + f_name
		
		urllib.request.urlretrieve(url, abs_url)
		image = File(open(abs_url, 'rb')) 

	if request.FILES:
		image = request.FILES.getlist('files')[0]
			
	(width, height) = get_size(image)

	img = Image.objects.create(img=image, height=height, width=width, name='default')
	img.name = img.img.path.split('\\')[-1]
	img.save()

	if request.POST.get('image_link'):
		image.close()
		try:
			os.remove(abs_url)
		except Exception as e:
			print(e)
	
	return redirect(img.get_absolute_url())	
	


def editImage(request):
	if request.method == "GET": 	
		name = request.path_info.split('/')[-1]	
		print(name)
		img = Image.objects.get(name = name)
		return render(request, 'edit_image.html', {'img': img})

	if not request.POST.get('width') and not request.POST.get('height'):
		name = request.META.get('HTTP_REFERER').split('/')[-1]		
		img = Image.objects.get(name = name)	
		messages.error(request, "Заполните хотя бы одно поле для изменения изображения")
		return redirect(img.get_absolute_url())	

	if request.POST.get('width') or request.POST.get('height'):
		width = request.POST.get('width')
		height = request.POST.get('height')

		name = request.META.get('HTTP_REFERER').split('/')[-1]		
		imge = Image.objects.get(name = name)		
		img = PILImage.open(imge.img.path)

		if not request.POST.get('height'):
			ratio = (imge.width / float(width))			
			height = int((float(imge.height) / float(ratio)))
			
		if not request.POST.get('width'):
			ratio = (imge.height / float(height))			
			width = int((float(imge.width) / float(ratio)))

		#Изменения размеров с соблюдением пропрорций
		resized_img = img.resize((int(width), int(height)), PILImage.ANTIALIAS)		
		path = ''
		path = path.join(imge.img.path.split('.')[:-1])
		new_img_path = path + uuid4().hex[:8] + '.' + imge.img.path.split('.')[-1]		
		resized_img.save(new_img_path)

		#Создание модели с новым файлом
		image = File(open(new_img_path, 'rb'))
		(width, height) = get_size(image)
		img_new = Image.objects.create(img=image, height=height, width=width, name='default')
		img_new.name = img_new.img.path.split('\\')[-1]
		img_new.save()
		image.close()
		try:
			os.remove(new_img_path)
		except Exception as e:
			print(e)

		return redirect(img_new.get_absolute_url())	

