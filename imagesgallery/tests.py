
from django.test import TestCase
from .models import Location,Image,Category
# Create your tests here.
# Test location class
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.argentina= Location(location = 'argentina')
    def test_instance(self):
        self.assertTrue(isinstance(self.argentina,Location))
        # Testing Save Method
    def test_save_method(self):
        self.argentina.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
          # Testing Delete Method


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.memes= Category(category = 'memes')
    def test_instance(self):
        self.assertTrue(isinstance(self.memes,Category))
        # Testing Save Method
    def test_save_method(self):
        self.memes.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
          # Testing Delete Method

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.myname= Image(image_name = 'myname', description = 'caligraphy')
    def test_instance(self):
        self.assertTrue(isinstance(self.myname,Image))
        # Testing Save Method
    def test_save_method(self):
        self.myname.save_image_name()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)
          # Testing Delete Method

