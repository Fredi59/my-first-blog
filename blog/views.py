# views from tutorial.djangogirls.org
# apla 03.04.2018 added code 30.40.2018 apla data templates

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Author

# Create your views here. 'Views' link models and templates together.
# views use Django ORM QuerieSets to retrieve data from the db
# Create a python function, that takes request as parameter
# post_list returns a function render that will 'render' = put together
# the Django template 'blog/post_list.html' a html website

def post_list(request):
    # posts = Post.objects.filter(published_date_lte=timezone.now().ordered_by('published_date'))
    # context = {}'posts': posts}  # use curled brackets
    posts = Post.objects.all()
    return render(request, 'blog\post_list.html', {'posts': posts})


# a improved post_list function retrieving all Post objects
# based on Django doc 2.0.4 example views 2.1.6 views
def post_list_all(request):
    a_list = Post.objects.all()  # save the Post objects  in a variable
    context = {'post_list_all': a_list}
    return render(request, 'blog\post_list.html', context)
