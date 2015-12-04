from django.db import models
from django.utils import timezone
from django.conf import settings


class Article(models.Model):
    title= models.CharField(max_length=200)
    author_name=models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    category= models.CharField(max_length=200)
    body=models.CharField(max_length=500)
    
    
    hero_image = models.ImageField(upload_to="uploads")
    optional_image = models.ImageField(upload_to="uploads",blank=True,null=True)


    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.title
# Create your models here.
