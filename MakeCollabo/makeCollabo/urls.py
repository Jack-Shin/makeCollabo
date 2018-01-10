from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^view-more/$', views.viewmore, name='viewmore'),
    url(r'addpost/$', views.addpost, name='addpost'),

    #for user auth
    url(r'^accounts/signup/$', views.signup, name='signup'),
]
