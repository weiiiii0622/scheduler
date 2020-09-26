from django.db import models

# Create your models here.

class Event(models.Model):
	STATUS = [
		('Done', 'Done'),
		('1/3 left', '1/3 left'),
		('Just started', 'Just started'),
		('Failed', 'Failed'),
		('Waiting', 'Waiting')
	]
	
	subject = models.CharField(max_length=20)
	description = models.TextField(max_length=100)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	clock = models.IntegerField()
	status = models.TextField(choices=STATUS, default='Waiting')

	def __str__(self):
		return self.subject





