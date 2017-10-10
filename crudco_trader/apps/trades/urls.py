from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'add', views.add, name = 'add'),
    url(r'create', views.create, name = 'create'),
    url(r'edit', views.edit, name = 'edit'),
    url(r'update', views.update, name = 'update'),
    url(r'delete/(?P<trade_id>[0-9])', views.delete, name = 'delete'),
    url(r'show/(?P<trade_id>[0-9])', views.show, name = 'show'),
    url(r'', views.read, name = 'read'),
    ]