from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighbourhood(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=30)
    count = models.IntegerField(default=0,blank=True) 
    
    def create_neighbourhood(self):
        self.save()
       
    
    def __str__(self):
        return self.name
class Profile(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    neighborhood = models.ForeignKey(Neighbourhood,null=True,on_delete=models.CASCADE) 
    
   
        
    def __str__(self):
        return self.name
    
class Business(models.Model):
    owner = models.CharField(max_length=40)
    business = models.CharField(max_length=200)
    business_email = models.EmailField(max_length=200)
    description = models.TextField(max_length=200)
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE) 
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def create_business(self):
        self.save()
     
    
    def __str__(self):
        return self.owner
        
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200) 
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        self.save()

    def __str__(self):
        return self.title
    
class Contacts(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    location = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name