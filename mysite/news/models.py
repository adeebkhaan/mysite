from django.db import models

# Create your models here.

class Reporter(models.Model):
	full_name = models.CharField(max_length=30)

	def __str__(self):
		return self.full_name

class Article(models.Model):
	date = models.DateField()
	headline = models.CharField(max_length=100)
	content = models.CharField(max_length=255)
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, related_name="Reporter")

	def __str__(self):
		return self.headline