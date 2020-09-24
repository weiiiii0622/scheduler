from django.db import models

# Create your models here.

class Event(models.Model):
	STATUS = [
		('1', 'Done'),
		('2', '1/3 left'),
		('3', 'Just started'),
		('4', 'Failed'),
		('5', 'Waiting')
	]
	
	subject = models.CharField(max_length=20)
	description = models.TextField(max_length=100)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	clock = models.IntegerField()
	status = models.TextField(choices=STATUS, default='5')

	def __str__(self):
		return self.subject





