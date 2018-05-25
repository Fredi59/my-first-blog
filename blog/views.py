# views from tutorial.djangogirls.org
# apla 03.04.2018 added code 30.40.2018 apla data templates
# views use Django ORM QuerySets to retrieve data from the db
# Create a python function, that takes request as parameter
# post_list returns a function render that will 'render' = put together
# the Django template 'blog/post_list.html' a html website

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from blog.models import Author


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
