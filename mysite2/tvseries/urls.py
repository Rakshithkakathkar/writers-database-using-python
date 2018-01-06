from django.conf.urls import url
from . import views

app_name = 'tvseries'

urlpatterns = [
#goes to /tvseries/
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),
    #goes to /tvseries/<Writer_id>/
    url(r'^(?P<writer_id>[0-9]+)/$', views.detail, name='detail'),
    #goes to tvseries/writer/add/
    url(r'^writer/add/$', views.create_writer, name='create_writer'),

    #goes to tvseries/writer/2/delete/
    url(r'^writer/(?P<writer_id>[0-9]+)/delete/$', views.delete_writer, name='delete_writer'),


    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^movies/(?P<filter_by>[a-zA_Z]+)/$', views.movies, name='movies'),

    #http://127.0.0.1:8000/tvseries/3/create_movie/
    url(r'^(?P<writer_id>[0-9]+)/create_movie/$', views.create_movie, name='create_movie'),
    url(r'^(?P<writer_id>[0-9]+)/delete_movie/(?P<movie_id>[0-9]+)/$', views.delete_movie, name='delete_movie'),

    url(r'^(?P<writer_id>[0-9]+)/create_tvshow/$', views.create_tvshow, name='create_tvshow'),
    url(r'^(?P<writer_id>[0-9]+)/delete_tvshow/(?P<tvshow_id>[0-9]+)/$', views.delete_tvshow, name='delete_tvshow'),

    


]