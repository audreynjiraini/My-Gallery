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
        
    
    @classmethod
    def get_all_locations(cls):
        '''
          Method to return all the locations.
        '''
        locations = cls.objects.all()
        return locations
    
    
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
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    
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
    
    
    @classmethod
    def get_image_by_id(cls,id):
        '''
          Method tto retrieve an image based on its id.
        '''
        image = cls.objects.get(id = id)
        return image
        
        
    @classmethod
    def search_by_category(cls,search_term):
        '''
          Method to search for images based on their category.
        '''
        images = cls.objects.filter(category__name__icontains = search_term)
        
        return images
        
    
    @classmethod
    def filter_by_location(cls,search_term):
        '''
          Method to filter images based on the location they were taken.
        '''
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images
    
    
    @classmethod
    def get_all_images(cls):
        '''
          Method to return all the images.
        '''
        images = cls.objects.all()
        return images
        
    
    class Meta:
        ordering = ['image_name']
    
    
    def __str__(self):
        return self.image_name
    