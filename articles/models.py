from django.db import models
from django.utils import timezone
from django.conf import settings


class Article(models.Model):
    title= models.CharField(max_length=200)                                          #to store article title
    author_name=models.CharField(max_length=50)                                      #to store the author's name of the title
    pub_date = models.DateTimeField('date published')                                #to store date of publication
    category= models.CharField(max_length=200)                                       #to store the category of the article
    body=models.CharField(max_length=500)                                            #to store the content of the article
    hero_image = models.ImageField(upload_to="uploads")                              #to store the main picture of the article ot the uploads folder in media
    optional_image = models.ImageField(upload_to="uploads",blank=True,null=True)     #to store the optional picture of the article ot the uploads folder in media


    
    def __unicode__(self):                                                           #str function of the Article class to represent an Article object                            
        return self.title

