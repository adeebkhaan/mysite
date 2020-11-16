from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
	return render(request, 'ADPCS/index.html')

def students(request):
	context = {
		'students': Student.objects.all()
	}
	return render(request, 'ADPCS/students.html', context)
def groups(request):
	context = {
		'groups': Group.objects.all()
	}
	return render(request, 'ADPCS/groups.html', context)
def student_details(request, id):
	groups = Group.objects.filter(members__id=id)
	context = {
		'student':Student.objects.get(pk=id),
		'groups':groups
	}
	return render(request, 'ADPCS/student_details.html', context)
def enroll(request):
	
	name = request.POST['name']
	email = request.POST['email']
	age = request.POST['age']

	student = Student.objects.create(name=name, email=email, age=age)
	student.save()

	return HttpResponseRedirect(reverse('ADPCS:students'))
def group_details(request, id):
	group = Group.objects.get(pk=id)
	context = {
		'group':Group.objects.get(pk=id),
		'members': group.members.all(),
		'non_members': Student.objects.exclude(group_members=group).all()
	}
	return render(request, 'ADPCS/group_details.html', context)
def add_member(request, id):
	member_id = int(request.POST['member'])
	student = Student.objects.get(pk=member_id)
	group = Group.objects.get(pk=id)

	group.members.add(student)

	return HttpResponseRedirect(reverse('ADPCS:group_details', args=(id,)))
