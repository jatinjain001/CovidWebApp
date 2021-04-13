from django.urls import path
from . import views
urlpatterns = [path('', views.helloworldview, name='home'),
               path('add', views.add, name='add')]
