from django.db import models
from django.utils import timezone
#from django.contrib.contenttypes.models import ContentType
#from django.contrib.contenttypes import generic

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return str(self.created_date)

class Image(models.Model):
    title = models.CharField(max_length=255)
    imgfile = models.ImageField(upload_to='img/')
    post = models.ForeignKey(Post)
   
    def image_img(self):
        if self.imgfile:
            return u'< img src="%s" width="100"/>' % self.imgfile.url
        else:
            return '(none)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

# Create your models here.
