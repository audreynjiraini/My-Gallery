from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    
    
    def save_location(self):
        '''
        Method to save location to the database.
        '''
        
        self.save()
        
    
    def delete_location(self):
        '''
        Method to delete location from the database.
        '''
        
        self.delete()
        
        
    def update_location(self, test):
        '''
          Method to update the location in the database.
        '''
        self.update(name = test)
    
    
    def __str__(self):
        return self.name
    
    

class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    
    def save_category(self):
        '''
        Method to save category to the database.
        '''
        
        self.save()
        
    
    def delete_category(self):
        '''
        Method to delete category from the database.
        '''
        
        self.delete()
        
        
    def update_category(self, test):
        '''
          Method to update the category in the database.
        '''
        self.update(name = test)
    
    
    def __str__(self):
        return self.name
    
      
   
class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    
    
    def save_image(self):
        '''
        Method to save image to the database.
        '''
        
        self.save()
        
    
    def delete_image(self):
        '''
        Method to delete image from the database.
        '''
        
        self.delete()
        
        
    def update_image(self, test):
        '''
          Method to update the image in the database.
        '''
        self.update(name = test)
        
    
    class Meta:
        ordering = ['image_name']
    
    
    def __str__(self):
        return self.image_name
    