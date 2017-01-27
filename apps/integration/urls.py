from django.conf.urls import url
# from . import views
from views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^show$', show, name='show'),
    # url(r'^register$', register, name='register'),
    # url(r'^success$', success, name='success'),
    # url(r'^logout$', logout, name='logout'),
]
