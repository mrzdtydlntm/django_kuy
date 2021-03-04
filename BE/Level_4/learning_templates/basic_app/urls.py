from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

#TEMPLATE TAGGING
app_name = 'basic_app'
urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]