from django.contrib import admin
from .models import Employee, Role, Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

'''with the help of admin.py we are registering our models into database and we will create a superuser to access
the portal with the command python manage.py createsuperuser'''
