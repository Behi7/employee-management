from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.StaffListCreateView.as_view(), name='Staff-list'),
    path('staff/<int:pk>/', views.StaffDetailUpdateDeleteView.as_view(), name='Staff-detail'),
    path('positions/', views.PositionListCreateView.as_view(), name='position-list-create'),
    path('positions/<int:pk>/', views.PositionDetailUpdateDeleteView.as_view(), name='position-update'),
    path('shifts/', views.ShiftListCreateView.as_view(), name='shift-list-create'),
    path('shifts/<int:pk>/', views.ShiftListCreateView.as_view(), name='shift-detail-update-delete'),
    path('staff-shifts/', views.StaffShiftListCreateView.as_view(), name='staffshift-list-create'),
    path('staff-shifts/<int:pk>/', views.StaffShiftDetailUpdateDeleteView.as_view(), name='StaffShiftupdate'),
    path('attandances/', views.StaffAttandanceListView.as_view(), name='attandance-list'),
]