from django import forms
from .models import Employee, Login

class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__self__(*args, **kwargs)
    #     self.fields['designation'].empty_label = "--Select--"
