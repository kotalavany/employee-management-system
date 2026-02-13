from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Employee

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'employees': employees})

from django.shortcuts import render, redirect
from .models import Employee

def add_employee(request):
    if request.method == "POST":
        print("POST DATA:", request.POST)  # 🔴 DEBUG LINE

        Employee.objects.create(
            employee_id=request.POST.get('employee_id'),
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            department=request.POST.get('department'),
            designation=request.POST.get('designation'),
            salary=request.POST.get('salary'),
            date_of_joining=request.POST.get('date_of_joining'),
        )

        return redirect('dashboard')  # stay on page for testing

    return render(request, 'add_employee.html')

# from django.http import HttpResponse

# def add_employee(request):
#     return HttpResponse("ADD EMPLOYEE VIEW HIT")


@login_required
def view_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    return render(request, 'view_employee.html', {'emp': emp})

@login_required
def edit_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        emp.name = request.POST['name']
        emp.email = request.POST['email']
        emp.phone = request.POST['phone']
        emp.department = request.POST['department']
        emp.designation = request.POST['designation']
        emp.salary = request.POST['salary']
        emp.save()
        return redirect('dashboard')
    return render(request, 'edit_employee.html', {'emp': emp})


@login_required
def delete_employee(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('dashboard')

