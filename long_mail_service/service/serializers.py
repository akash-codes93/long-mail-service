from rest_framework import serializers
from long_mail_service.models import *


class TrainSerializer(serializers.ModelSerializer):
    unit_cost = serializers.FloatField()

    class Meta:
        model = Train
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    end_time = serializers.DateTimeField()

    class Meta:
        model = Trip
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'
