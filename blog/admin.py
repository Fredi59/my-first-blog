# from django.contrib import admin

# Register your models here.

# apla changed 24.03.2018

from django.contrib import admin
from .models import Post

admin.site.register(Post)
