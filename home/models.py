from django.db import models

class Person(models.Model):
    Username = models.CharField(max_length=100)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Gender = models.CharField(max_length=7)
    Phone_number = models.CharField(max_length=15)
    
    def __str__ (self):                     
        return self.Username  #This returns the Person's Username upon calling from another Table/Model as a default

#models.PROTECT in order to know how to find member if they leave
#default=1 because database needs something to populate existing rows to call to class Person
#Many-to-One relationship with Person
class Addresse(models.Model):
    House_number = models.CharField(max_length=4)
    Street_name = models.CharField(max_length=1000)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Address_owner = models.ForeignKey(Person, on_delete=models.PROTECT, default=1)
    


#default=1 because database needs something to populate existing rows to call to class Person
#Many-to-One relationship with Person
class Doctor(models.Model):
    Fullname = models.CharField(max_length=100)
    Address = models.CharField(max_length=1000)
    Hospital = models.CharField(max_length=100)
    Patient = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
   


#default=1 because database needs something to populate existing rows to call to class Person
class Product(models.Model):
    Size = models.IntegerField()
    product_color = models.CharField(max_length=40)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()

#default=1 because database needs something to populate existing rows to call to class Person
#One-to-One relationship with Person
class Bio(models.Model):
    Bio_content = models.CharField(max_length=200)
    Author = models.OneToOneField(Person, on_delete=models.CASCADE, default=1)
    Last_updated = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    
'''See account app for task7.py'''