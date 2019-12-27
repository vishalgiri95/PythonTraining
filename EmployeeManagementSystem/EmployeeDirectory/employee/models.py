from django.db import models

class Designation(models.Model):
    title = models.CharField(max_length = 30)

class Login(models.Model):
    username = models.CharField(max_length=20, unique = True)
    password = models. CharField(max_length=20)

LOCATION = (
    ('mumbai','MUMBAI'),
    ('bangalore', 'BANGALORE'),
    ('pune','PUNE'),
    ('hyderabad','HYDERABAD'),
    ('kolkata','KOLKATA'),
)

class Employee(models.Model):
    full_name   = models.CharField(max_length = 25)
    email_id    = models.EmailField(max_length = 50, unique = True)
    username    = models.CharField(max_length = 20, unique = True)
    mobile_no   = models.CharField(max_length = 10)
    location    = models.CharField(max_length = 10, choices = LOCATION, default = 'Mumbai')
    designation = models.ForeignKey(Designation, on_delete = models.CASCADE)


    def __str__(self):
        return self.full_name
