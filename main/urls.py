from django.urls import path, include
from . import views

urlpatterns = [
    path('attadance', include('main.attadance.urls')),
    path('', views.main, name='index'),
    path('listposition', views.listPosition, name='listposition'),
    path('createposition', views.createPosition, name='createposition'),
    path('updateposition/<int:id>', views.updatePosition, name='updateposition'),
    path('deleteposition/<int:id>', views.deletePositon, name='deletepositon'),
    path('staffcreate', views.createStaff, name='createstaff'),
    path('stafflist', views.staffList, name='stafflist'),
    path('staffupdate/<int:id>', views.staffUpdate, name='staffupdate'),
    path('staffdelete/<int:id>', views.staffDelete, name='staffdelete'),
    path('log-in', views.login_user, name='login'),
    path('log-out', views.log_out, name='logout'),
    path('visit', views.visitList, name='visitlist'),
    path('listshift', views.listShift, name='listshift'),
    path('deleteshift/<int:id>', views.deleteshift, name='deleteshift'),
    path('createshift', views.createShift, name='createshift')
]