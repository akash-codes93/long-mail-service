from typing import List
from datetime import timedelta

from django.db.models.functions import Now

from long_mail_service.models import Trip
from long_mail_service.service.serializers import TripSerializer


class TripService:

    @staticmethod
    def create_trip(train_id: int, line_id: int) -> int:
        """
        create a trip to deliver parcels
        """
        trip = Trip.objects.create(train_id=train_id, line_id=line_id)
        trip.save()
        return TripSerializer(trip).data

    @staticmethod
    def complete_trips(trip_length=3) -> None:
        """
        Mark all the trips completed whose start_time > 3 minutes
        """
        trips = Trip.objects.filter(start_time__lt=Now() - timedelta(minutes=trip_length))
        for trip in trips:
            trip.is_completed = True
            trip.save()

    @staticmethod
    def get_trip_details(trip_id):
        """
        Get all trip details using trip id
        """
        try:
            trip = Trip.objects.get(id=trip_id)
            return TripSerializer(trip).data
        except Trip.DoesNotExist:
            return None

    @staticmethod
    def get_trip_details_using_train_id(train_id: int) -> List:
        """
        Get all trip details using train_id
        """
        trips = Trip.objects.filter(train_id=train_id)
        return TripSerializer(trips, many=True).data


trip_service = TripService()
