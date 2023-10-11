from typing import List

from long_mail_service.models import Booking
from long_mail_service.service.serializers import BookingSerializer


class BookingService:

    @staticmethod
    def create_booking(trip_id: int, parcel_id: int, cost: int, strategy_name: str) -> int:
        booking = Booking.objects.create(trip_id=trip_id, parcel_id=parcel_id, cost=cost, strategy=strategy_name)
        booking.save()

        return BookingSerializer(booking).data

    @staticmethod
    def get_bookings_from_trip(trip_id) -> List:
        """
        Get booking details from trip
        """
        bookings = Booking.objects.select_related('parcel').filter(trip_id=trip_id)
        return BookingSerializer(bookings, many=True).data

    @staticmethod
    def get_booking_from_parcel(parcel_id):
        """
        Get booking details from trip
        """
        try:
            bookings = Booking.objects.get(parcel_id=parcel_id)
            return BookingSerializer(bookings).data
        except Booking.DoesNotExist:
            return None


booking_service = BookingService()
