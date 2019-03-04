from django.db import models

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location):
        location = cls.objects.get(pk=id)
        location = cls(location=location)
        location.save()


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.category
    class Meta:
        ordering = ['category']
        verbose_name_plural = 'Categories'

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,category):
        category = cls.objects.get(pk=id)
        category = cls(category=category)
        category.save()

# adding image category
# adding image class
class Image(models.Model):
    image_name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    photo = models.ImageField(upload_to = 'index/')

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,name,description,location,category):
        image = cls.objects.get(pk=id)
        image = cls(name=name,description=description,location=location,category=category)
        image.save()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(pk=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
# search image 
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category=search_term)
        return images

class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location
    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,location):
        location = cls.objects.get(pk=id)
        location = cls(location=location)
        location.save()

# adding image category


    