# this is a new file in the blog directory
# tutorial.djangogirls.org apla 02.04.2018
# from django.urls import url  # see Django doc 2.0.4
# the django doc example uses the path module instead of url
# from django.urls import path
# p.10 urls.py >> import errror
from django.conf.urls import url

# import all our views from the blog app
from   .  import views
# Django webserver error 'cannot import name views'
# added more space in line 6

# add urlpatterns
# the regex declares that only an empty string will match
# Django will look up the post_list function in views
# instead of url() use path() see django doc 2.0.4 example 2.1.5
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # added a new views callback function apla 01.05.2018
    url(r'^$', views.post_list_filter, name='post_list_filter'),
]
