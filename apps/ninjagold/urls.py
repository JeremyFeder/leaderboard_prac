from django.conf.urls import url
from views import index, process, logout, save

urlpatterns = [
    url(r'^process_gold$', process, name='process_g'),
    url(r'^logout$', logout, name='logout'),
    url(r'^save$', save, name='save'),
    url(r'^$', index, name='index'),
]
