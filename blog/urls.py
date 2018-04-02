# this is a new file in the blog directory
# tutorial.djangogirls.org apla 02.04.2018
# from django.urls import url  # see Django doc 2.0.4
# p.10 urls.py >> import errro
from django.conf.urls import url

# import all our views from the blog app
from   .  import views
# Django webserver error 'cannot import name views'
# added more space in line 6

# add urlpatterns
# the regex declares that only an empty string will match
# Django will look up the post_list in views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
