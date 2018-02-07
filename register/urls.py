from django.conf.urls import url
from .views import *
from . import views
app_name='register'

urlpatterns = [
    url(r'^$',views.index.as_view(),name='index'),
    url(r'^register',UserFormView.as_view(),name='register'),
    url(r'^login$',Login,name='login'),
    url(r'^temp$',temp,name='temp')
]

