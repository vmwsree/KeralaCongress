from django.db import models

# Create your models here.


class tags(models.Model):
    tagname = models.TextField(default='uncatgorised',max_length=30,unique=True)
    def __unicode__(self):
        return self.tagname

class images(models.Model):
    date = models.DateTimeField()
    title = models.TextField(default='image',max_length=30,blank=True)
    caption = models.TextField(default="Kerala Congress",max_length="100")
    image = models.ImageField(upload_to="uploads")
    tag = models.ManyToManyField(tags)
    def __unicode__(self):
        return self.title

class keralaYatra(models.Model):
    date = models.DateField(unique=True,default=12/12/12)
    time = models.CharField(max_length=4,blank=True)
    images = models.ManyToManyField(images,blank=True)
    title = models.CharField(max_length=100,unique=True,default="Kerala Congress")
    description = models.CharField(max_length=1000,default="sample text",blank=True)
    maplan = models.CharField(max_length=1000,default="3423",blank=True)
    maplon = models.CharField(max_length=1000,default="3423",blank=True)
    def __unicode__(self):
        return str(self.title)

class Post(models.Model):
    Image = models.ManyToManyField(images,blank=True)
    Title = models.CharField(max_length="200",default="Post")
    contet = models.CharField(max_length=4000,blank=True)
    date = models.DateField(default=12/12/12)
    tag = models.ManyToManyField(tags)
    def __unicode__(self):
        return self.Title
class homepage(models.Model):
    slider_content= models.CharField(max_length=4000,blank=True)
    sliderimage = models.ImageField(upload_to="uploads")