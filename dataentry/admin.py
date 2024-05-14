from django.contrib import admin

from .models import Customer, Student

admin.site.register(Student)
admin.site.register(Customer)
