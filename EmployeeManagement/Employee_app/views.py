from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index (request):        # With the help of this function we are trying to create a webpage by passing html file
    return render(request, 'index.html') # With this we have checked if our routing working propely or not

def all_emp (request):
    emps = Employee.objects.all()            # to check all the employees in a model
    context = {                              # context is like a dictionary in Django
        'emps' : emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context) # to route at the end of html file

def add_emp (request):
    if request.method == 'POST':        # extracting parameters from POST method
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        depart = int(request.POST['depart'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name = first_name, last_name = last_name, salary = salary, bonus=bonus, phone=phone, depart_id = depart, 
                 role_id = role, hire_date = datetime.now())   # adding a new employee after mentioning required parameters
        new_emp.save()
        return HttpResponse('Employee Added Successfully!')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception has occured!")
     

def remove_emp (request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed= Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Please Enter a valid Emp ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
        
    }
    return render(request, 'remove_emp.html',context)

def filter_emp (request):
    if request.method == 'POST':
        name = request.POST['name']
        depart = request.POST['depart']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if depart:
            emps = emps.filter(depart__name__icontains = depart)
        if role:
            emps = emps.filter(role__name__icontains = role)
        
        context = {
            'emps':emps
            
        }
        return render(request, 'view_all_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An Exception has occured!")
        
        
    