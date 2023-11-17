from django.db import models

# Create your models here.
# With the help of models we are creating a database in which we will be stroing our information

class Department(models.Model): # As working department can be same so we will create a separate model 
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)
    
    def __str__(self): # this function will help us to display name on our portal
        return self.name
    
class Role(models.Model): # Same with role as well 
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    depart = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone) # %s is a place holder
    
'''As we are creating these models we need to make sure we migrate this to project (0001_initial.py) with the help
of python manage.py makemigrations'''
'''we also have to migrate this file into database to store it permanently with the help of 
python manage.py migrate command'''
'''whenever you are updating this file just make sure you are migrating it'''