from django.urls import path
from . import views

app_name = 'ADPCS'

urlpatterns = [
	path('', views.index, name='index'),
	path('students', views.students, name='students'),
	path('groups', views.groups, name='groups'),
	path('student/<int:id>', views.student_details, name='student_details'),
	path('enroll', views.enroll, name='enroll'),
	path('group/<int:id>', views.group_details, name='group_details'),
	path('add_member_to_this_group/<int:id>', views.add_member, name='add_in_group'),
]