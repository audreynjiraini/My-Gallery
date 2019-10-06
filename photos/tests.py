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
        
        
    