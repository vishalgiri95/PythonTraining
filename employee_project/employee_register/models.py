from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullName = models.CharField(max_length = 100)
    empCode = models.CharField(max_length = 6)
    mobileNo = models.CharField(max_length = 10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE )

    def __str__(self):
        return self.fullName
        
