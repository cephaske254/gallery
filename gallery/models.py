from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=30)

class Category(models.Model):
    category = models.CharField(max_length=30)

class Post(models.Model):
    image = models.ImageField(upload_to='articles/',default='none')
    image_caption = models.TextField() #image description
    image_category = models.ManyToManyField(Category)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

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
