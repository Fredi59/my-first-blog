# this is a new file in the blog directory
# tutorial.djangogirls.org apla 02.04.2018
# from django.urls import url  # see Django doc 2.0.4
# the django doc example uses the path module instead of url
# from django.urls import path
# p.10 urls.py >> import errror
# added a new urlpattern 'post_new' using django forms
# apla 25.05.2018 djangoGirls 'django forms'

from django.conf.urls import url
# import all our views from the blog app
# from . import views
from blog import views

# Django webserver error 'cannot import name views'
# added more space in line 6

# add urlpatterns - django passes through the list of urlpatterns
# django renders the first url that matches
# the regex declares that only an empty string will match
# Django will look up the post_list function in views.py
# instead of url() use path() see django doc 2.0.4 example 2.1.5
urlpatterns = [
    # reminder: care for the 'Reihenfolge' the ranking
    url(r'^$', views.post_list, name='post_list'),
    # added apla 23.05.18 to point to a post_detail template website
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # added a new url pattern 25.05.2018 apla to use django forms
    url(r'^post/new/$', views.post_new, name='post_new'),
    # added a new views callback function apla 01.05.2018
    # changed regex r'^$' against ''  apla 15.05.2018
    url('', views.post_list_filter, name='post_list_filter'),
    url(r'^$', views.post_list_all, name='post_list_all'),


]
