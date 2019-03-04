from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
class Upload(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ForeignKey(Editor)
    pub_date = models.DateTimeField(auto_now_add=True)
    upload_image = models.ImageField(upload_to = 'index/')

    