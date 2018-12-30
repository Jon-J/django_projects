from django.conf.urls import url
from . import views

app_name = 'philatelist'

urlpatterns = [
    # Home page /philatelist/
    url(r'^$', views.index, name="index"),

    # Album detail /philatelist/:id/
    url(r'^(?P<stamps_group_id>[0-9]+)/$', views.detail, name="detail"),

    # API for favourite a song /music/:id/favourite/
    #url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite"),

]
