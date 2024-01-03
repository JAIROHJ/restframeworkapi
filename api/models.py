from django.db import models

# Create your models here.
#Company Model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NON IT','NON IT'),('MOBILE PHONE','MOBILE PHONE')))
    added_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' ' + self.location

#Employee Model

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(('Manager','Manager'),('Forntend Developer','Forntend Developer'),('Backend Developer','Backend Developer'),('Project Leader','Project Leader')))

    company=models.ForeignKey(Company,on_delete=models.CASCADE)