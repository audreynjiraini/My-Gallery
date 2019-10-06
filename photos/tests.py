from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.

class LocationTestClass(TestCase):
    '''
    Tests for Location class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.location = Location(id = 50, name = 'Kenya')
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Location class.
        '''
        
        self.assertTrue(isinstance(self.location, Location))
        
        
    def test_save_method(self):
        '''
        Test whetherthe object is saved in the database.
        '''
        
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
        
    def test_update_method(self):
        '''
        Test if the object can be updated.
        '''
        self.location.save_location()
        self.location = Location.objects.filter(name = 'Kenya').update(name = 'Burundi')
        self.updated_location = Location.objects.get(name = 'Burundi')
        self.assertEqual(self.updated_location.name,"Burundi")


    def test_delete_method(self):
        '''
        Test if the object can be deleted from the database.
        '''
        self.location.save_location()
        self.location = Location.objects.get(id = 50)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)