from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    #path('add', views.add, name = 'add'),
    #path('mul', views.mul, name = 'mul'),
    path('cal',views.cal, name = 'cal')
]