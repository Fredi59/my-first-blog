# from django.db import models
# Create your models here.

from django.db import models
from django.utils import timezone
# django 2.0 changed import of 'User' attribute
from django.contrib.auth.models import User

# my model Author - aded by apla 23.04.2018 to replace
# the ForeignKey author powered by authors.User from the Djang manage.py
class Author(models.Model):
    """docstring for [class Author]."""
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name   #


# my model POST
class Post(models.Model):
    """docstring for [class Post]."""
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title   # self.author
