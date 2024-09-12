from rest_framework import serializers
from main.models import Staff, Position, Shift, StaffShift, StaffAttandance

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = '__all__'


class StaffAttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttandance
        fields = '__all__'