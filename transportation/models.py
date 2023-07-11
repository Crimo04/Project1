from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True,)
    username= models.CharField(max_length=135)
    email= models.EmailField(max_length=254)
    password= models.CharField(max_length=30)

class Role(models.Model):

    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_name= models.CharField(max_length=50,choices=[('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Passenger', 'Passenger'),
        ('Driver', 'Driver'),])


