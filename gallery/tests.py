from django.test import TestCase
from .models import Post,Category,Location
# Create your tests here.
class GalleryTestClass(TestCase):
    def setUp(self):
        self.new_category  = Category(category='adventure')
        self.new_category.save()
        self.new_location = Location(location='test')
        self.new_location.save()
        self.new_post = Post(image='test.png',image_caption='caption...', image_location=self.new_location)
        self.new_post.save()
        self.new_post.image_category.add(self.new_category)
    
    def test_save_post(self):
        self.assertTrue(len(Post.get_all())> 0)

    def test_delete_post(self):
        self.new_post.delete()
        self.assertEqual(len(Post.get_all()),0)

    def test_search_image(self):
        post = Post.objects.filter(image_category=self.new_category)
        self.assertTrue(len(post)== 1)
    
    def test_get_image_by_id(self):
        post = Post.search_image(self.new_category).first()
        self.assertTrue(post)

    def test_filter_by_location(self):
        post = Post.filter_by_location((self.new_location))
        self.assertTrue(post)

    def tearDown(self):
        Post.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
