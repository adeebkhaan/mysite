from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=64)
	email = models.EmailField(max_length=64)
	age = models.IntegerField()
	

	def __str__(self):
		return f"{self.id} : {self.name}"

class Group(models.Model):
	name = models.CharField(max_length=64)
	members = models.ManyToManyField(Student, blank=True, related_name='group_members')
	created_at = models.DateTimeField()

	def __str__(self):
		return f"{self.name}"

