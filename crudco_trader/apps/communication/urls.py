from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create/(?P<trade_id>[0-9]+)', views.create, name = 'create'),
    url(r'^read/(?P<message_id>[0-9]+)', views.read, name = 'read'),
    url(r'^review/(?P<user_id>[0-9]+)', views.review, name = 'review'),
    url(r'^update', views.update, name = 'update'),
    url(r'^delete', views.delete, name = 'delete'),
    ]