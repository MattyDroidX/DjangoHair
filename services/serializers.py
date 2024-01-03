from rest_framework import serializers
from .models import HairSalon, OpeningHours, TimeSlot, Service

class HairSalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HairSalon
        fields = '__all__'

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

