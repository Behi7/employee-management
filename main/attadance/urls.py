from django.urls import path
from . import views

urlpatterns = [
    path('', views.listAttadance, name='listattadance'),
    path('create/<int:id>', views.createAttadance, name = 'createattadance')
]