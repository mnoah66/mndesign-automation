from django.contrib import admin

from django.contrib import admin
from .models import employees, empgroups

class employeesAdmin(admin.ModelAdmin):
	list_display=('fname', 'lname', 'email', 'phone_number', 'group')
class empgroupsAdmin(admin.ModelAdmin):
	list_display=('title')
admin.site.register(employees, employeesAdmin)
admin.site.register(empgroups)

