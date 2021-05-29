from rest_framework import serializers
from .models import Passenger

class PassengerSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields=['id', 'name', 'rewardpoints']
