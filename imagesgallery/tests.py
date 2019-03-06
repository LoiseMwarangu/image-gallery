
from django.test import TestCase
from .models import Location,Image,Category
# Create your tests here.
# Test location class
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.argentina= Location(id=1 ,location = 'argentina')
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
        self.memes= Category(id=1 ,category = 'memes')
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
        self.image = Image(id='1', image_name='name', description ='this photo', location='        self.image = Image(id='1', image_name='name', description ='this photo', location=self.locale, photo='test.jpg')
', photo='test.jpg')
    def test_instance(self):
        self.assertTrue(isinstance(self.myname,Image))
        # Testing Save Method
    def test_save_method(self):
        self.myname.save_image_name()
        photos = Image.objects.all()
        self.assertTrue(len(photos) > 0)
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()

    def test_update_method(self):
        self.image.save_image()
        new_image = Image.objects.filter(photo='test.jpg').update(photo='banana.jpg')
        images = Image.objects.get(photo='banana.jpg')
        self.assertTrue(images.photo, 'banana.jpg')

    def test_get_image_by_id(self):
        self.image.save_image()
        this_img= self.image.get_image_by_id(self.image.id)
        image = Image.objects.get(id=self.image.id)
        self.assertTrue(this_img, image)


