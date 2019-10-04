from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    

class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    
    def __str__(self):
        return self.name
    
      
   
class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    
    
    def __str__(self):
        return self.image_name
    
    
    class Meta:
        ordering = ['image_name']