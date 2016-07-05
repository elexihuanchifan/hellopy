from django.conf.urls import patterns, url

urlpatterns = [
    url(r'^staff/', 'west.views.staff'),
    url(r'^templay/', 'west.views.templay'),
]
