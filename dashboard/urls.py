from django.urls import path
from . import views
#from adminlte3 import views


urlpatterns = [
    path('', views.index, name='index'),

]
