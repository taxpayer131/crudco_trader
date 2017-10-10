from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'logout', views.logout, name = 'logout'),
    url(r'delete', views.delete, name = 'delete'),
    url(r'profile', views.profile, name = 'profile'),
    url(r'create', views.create, name = 'create'),
    url(r'new', views.new, name = 'new'),
    url(r'login', views.login, name = 'login'),
    url(r'', views.index, name = 'index'),
]