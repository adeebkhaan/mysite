from django.contrib import admin
from .models import *

class GroupAdmin(admin.ModelAdmin):
	list_display = ('name','created_at',)
	ordering = ['id']

class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	ordering = ['id']

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)