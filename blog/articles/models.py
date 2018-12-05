from django.db import models

# Create your models here.
# models start with capitals


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    # careful, each function inside class needs
    # indentation tab to belong to class
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + " ..."
