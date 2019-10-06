from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    
    
    def save_location(self):
        '''
        Method to save location to the database
        '''
        
        self.save()
    
    
    def __str__(self):
        return self.name
    
    

class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    
    def save_category(self):
        '''
        Method to save category to the database
        '''
        
        self.save()
    
    
    def __str__(self):
        return self.name
    
      
   
class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    
    
    def save_image(self):
        '''
        Method to save image to the database
        '''
        
        self.save()
        
    
    class Meta:
        ordering = ['image_name']
    
    
    def __str__(self):
        return self.image_name
    