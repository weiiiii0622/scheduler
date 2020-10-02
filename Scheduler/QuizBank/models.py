from django.db import models

# Create your models here.

class Quiz(models.Model):

	subject = models.CharField(max_length=50)
	year = models.TextField()
	question = models.TextField()

	option1 = models.TextField(null=True)
	option2 = models.TextField(null=True)
	option3 = models.TextField(null=True)
	option4 = models.TextField(null=True)
	option5 = models.TextField(null=True)
	option6 = models.TextField(null=True)
	option7 = models.TextField(null=True)
	option8 = models.TextField(null=True)
	option9 = models.TextField(null=True)
	option10 = models.TextField(null=True)
	option11 = models.TextField(null=True)
	option12 = models.TextField(null=True)
	option13 = models.TextField(null=True)
	option14 = models.TextField(null=True)
	option15 = models.TextField(null=True)

	answer = models.TextField()
	
	def __str__(self):
		return self.subject
	