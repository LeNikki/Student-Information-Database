#app1 url
from django.urls import path
from . import  views

urlpatterns = [
    path('home', views.std, name = 'home'),            #this is for addding student
    path('data', views.data, name = 'data'),          #showing all data
    path('delete/<int:no_field>', views.delete, name = 'delete'), #delete by #
    path('edit/<int:no_field>', views.edit, name = 'edit'), #delete by #
    path('search', views.search, name = 'search'), #delete by #
    
]
