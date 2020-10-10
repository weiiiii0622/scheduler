from django.db import models

# Create your models here.

class Quiz(models.Model):

	subject = models.CharField(max_length=50, null=True, blank=True)
	year = models.TextField(null=True, blank=True)
	
	question1 = models.TextField(null=True, blank=True)
	question2 = models.TextField(null=True, blank=True)
	question3 = models.TextField(null=True, blank=True)

	image1 = models.TextField(null=True, blank=True)
	image2 = models.TextField(null=True, blank=True)
	image3 = models.TextField(null=True, blank=True)


	option1 = models.TextField(null=True, blank=True)
	option2 = models.TextField(null=True, blank=True)
	option3 = models.TextField(null=True, blank=True)
	option4 = models.TextField(null=True, blank=True)
	option5 = models.TextField(null=True, blank=True)
	option6 = models.TextField(null=True, blank=True)
	option7 = models.TextField(null=True, blank=True)
	option8 = models.TextField(null=True, blank=True)
	option9 = models.TextField(null=True, blank=True)
	option10 = models.TextField(null=True, blank=True)
	option11 = models.TextField(null=True, blank=True)
	option12 = models.TextField(null=True, blank=True)
	option13 = models.TextField(null=True, blank=True)
	option14 = models.TextField(null=True, blank=True)
	option15 = models.TextField(null=True, blank=True)

	answer = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return self.subject
	