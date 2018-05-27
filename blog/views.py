# views from tutorial.djangogirls.org
# apla 03.04.2018 added code 30.40.2018 apla data templates
# views use Django ORM QuerySets to retrieve data from the db
# Create a python function, that takes request as parameter
# post_list returns a function render that will 'render' = put together
# the Django template 'blog/post_list.html' a html website
# https://docs.djangoproject.com/en/2.0/topics/forms/ 26.05.18 apla

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.models import Author

# use django forms apla 25.50.2018 import the PostForm class
from .forms import PostForm  # ModuleNotFoundError  no module named blog.forms

# Create your views here. 'Views' link models and templates together.

def post_list(request):
    # posts = Post.objects.filter(published_date_lte=timezone.now().ordered_by('published_date'))
    # context = {}'posts': posts}  # use curled brackets
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# a post_list function retrieving all Post objects and storing results in a variable
# based on Django doc 2.0.4 example views 2.1.6 views
def post_list_all(request):
    post_list_all = Post.objects.all()  # save the Post objects  in a variable
    # context = {'post_list_all': post_list_all}
    # return render(request, 'blog/post_list.html', context)
    return render(request, 'blog/post_list.html', {'post_list_all': post_list_all})

# a post_list function filtering Post objects
# based on Django doc 2.0.4 example views 2.1.6 views
def post_list_filter(request):
    post_list_filter = Post.objects.filter(title__contains='Django')
    # context1 = {'post_list_filter_title': post_list_filter_title} # urls.py error 'no attribute'
    return render(request, 'blog/post_list_filter.html', {'post_list_filter': post_list_filter})

# a post_list function filtering Post objects
# based on DjangoGirls tutorial views 2.1.6 views apla 23.05.2018
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# added a callback function for the django new post form apla 25.05.18
def post_new(request):
    # save the new form using the POST method if the entries are valid
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = Author.full_name  # added a third form attribute 'author' in forms.py
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    # if a GET (or any other method) will create a blank form
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# added a callback function for the django post edit form apla 27.05.18
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # save the new form using the POST method if the entries are valid
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = Author.full_name  # added a third form attribute 'author' in forms.py
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    # if a GET (or any other method) will create a blank form
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
