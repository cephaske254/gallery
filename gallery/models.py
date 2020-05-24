from django.db import models
from photogallery.settings import MEDIA_URL
import pyperclip

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Post(models.Model):
    image = models.ImageField(upload_to='article_images/',default='none')
    image_caption = models.TextField() #image description
    image_category = models.ManyToManyField(Category)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_caption

    @classmethod
    def get_all(cls):
        all=cls.objects.all()
        for one in all:
            print(one.image.url)
        return all 

    def save_post(self):
        self.save()

    def delete_post(self):
        self.new_post.delete()
    
    def search_image(self,category):
        post = Post.objects.filter(image_category=category)
        return post
    
    def get_image_by_id(self,id):
        post = Post.objects.filter(pk=id)
        return post

    def filter_by_location(self,location):
        post = Post.objects.filter(image_location=location)
        return post
    
    @classmethod
    def copy_link(cls, host,id):
        post = cls.objects.filter(pk=id).first()
        location = post.image.url
        link=host+location
        pyperclip.copy(link)
        return link


