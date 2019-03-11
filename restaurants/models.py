from django.db import models
from django.contrib.auth.models import User
from .snippets import generate_unique_slug, choices
from django.utils.text import slugify

class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='restaurants/')
    categories = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    price = models.IntegerField()
    vat = models.PositiveIntegerField(default=0)
    taste = models.PositiveIntegerField(choices=choices)
    persons = models.PositiveIntegerField(choices=choices)
    details = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    views = models.IntegerField(default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

    def get_categories(self):
        cats = self.categories.split(',')
        return cats

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Restaurant, self.title)
        else:  # create
            self.slug = generate_unique_slug(Restaurant, self.title)
        super().save(*args, **kwargs)

    def delete(self,*args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:100]
