from django.db.models import *
from PIL import Image as PILImage
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

def get_size(file):
	im = PILImage.open(file)
	(width, height) = im.size
	return width, height

class Image(Model):	
	name = CharField('Имя', max_length=255, null=True, blank=True, unique=True)
	img = FileField('Изображение', max_length=255, null=True)
	width = PositiveSmallIntegerField('Ширина', null=True, blank=True)
	height = PositiveSmallIntegerField('Высота', null=True, blank=True)	
	url = URLField('URL', max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Image, self).save(*args, **kwargs)
		
		if not self.width and not self.height:
			(self.width, self.height) = get_size(self.img)			
			super(Image, self).save(*args, **kwargs)

		if not self.name:
			self.name = self.img.path.split('\\')[-1]
			super(Image, self).save(*args, **kwargs)	

	def get_absolute_url(self):
		return '/edit_image/{}'.format(self.name)

	class Meta:
		verbose_name = 'Изображние'
		verbose_name_plural = 'Изображения'


