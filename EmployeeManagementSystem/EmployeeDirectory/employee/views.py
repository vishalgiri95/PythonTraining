from django.shortcuts import render
from .forms import LoginForm, EmployeeForm
from .models import Employee
from .models import Login


def login(request):
    if request.method == 'GET':
        form  = LoginForm()
    return render(request, "employee/login.html", {'form' : form})

def signup(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, "employee/signup.html", {'form' : form})

    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "employee/success.html")
