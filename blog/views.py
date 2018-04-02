# views from tutorial.djangogirls.org
# apla 03.04.2018
from django.shortcuts import render

# Create your views here.
# a python function that takes request as parameter
# post_list returns a function render that will render = put together
# the Django template 'blog/post_list.html'
def post_list(request):
    return render(request, 'blog\post_list.html', {})
