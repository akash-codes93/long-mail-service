"""
Unit Test cases related to booking service
"""
from django.test import TestCase

from long_mail_service.models import Booking

from long_mail_service.service.line import line_service
from long_mail_service.service.train import train_service
from long_mail_service.service.trip import trip_service
from long_mail_service.service.booking import booking_service
from long_mail_service.service.parcel import parcel_service


class TestBookingService(TestCase):

    def test_booking_service(self):

        train = train_service.create_train("train-A", 23, 1265, 12357, ["A", "B"])

        trip = trip_service.create_trip(train["id"], train["lines"][0])
        parcel = parcel_service.create_parcel(10, 10)

        booking = booking_service.create_booking(trip["id"], parcel["id"], 200)

        exists = True
        try:
            booking = Booking.objects.get(id=booking["id"]).id
        except Booking.DoesNotExist:
            booking = None
            exists = False

        bookings = booking_service.get_bookings_from_trip(trip["id"])

        self.assertEqual(exists, True)
        self.assertEqual(booking, bookings[0]["id"])

