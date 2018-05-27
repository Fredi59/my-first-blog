# djangoGirls tutorial 'django forms'
# use the form in a view and display it in a templates
# create a link to the page post_edit.html, create
# create a url, a view and a template post_edit.html
# added apla 25.05.2018

from django import forms

from blog.models import Post
from .models import Author

# class PostForm(forms.Form):
class PostForm(forms.ModelForm):
    # title = forms.CharField(label='Title', help_text="Enter a title as text", max_length=100)
    class Meta:
        model = Post
        # djangoGirls tutorial uses just 'title' and 'text'
        # apla 27.05.18 added 'author' to solve views.py post.save()
        # Integrity Error ap /pos/new/ exception NOT NULL constrained failed
        fields = ('title', 'text', 'author')
