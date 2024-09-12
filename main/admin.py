from django.contrib import admin
from . import models


class StaffAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'age', 'number', 'position') 
    search_fields = ('f_name', 'l_name', 'number') 
    list_filter = ('position', 'age')  


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)


class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_start', 'time_stop')
    search_fields = ('name', 'time_start', 'time_stop') 
    list_filter = ('time_start', 'time_stop')


class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ('staff', 'shift')
    search_fields = ('staff', 'shift') 
    list_filter = ('staff', 'shift')


class StaffAttandanceAdmin(admin.ModelAdmin):
    list_display = ('detatime', 'staff')
    search_fields = ('detatime', 'staff') 
    list_filter = ('detatime', 'staff')


admin.site.register(models.Staff, StaffAdmin)
admin.site.register(models.StaffAttandance)
admin.site.register(models.StaffShift, StaffShiftAdmin)
admin.site.register(models.Shift, ShiftAdmin)
admin.site.register(models.Position, PositionAdmin)