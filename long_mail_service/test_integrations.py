"""
Integration test for api and service layer
"""
from django.test import TestCase
from long_mail_service.api import *
from long_mail_service.service.line import line_service


class TestTrainAPI(TestCase):

    def test_train_api(self):
        train = TrainAPI.create_train("train-A", 23, 1265, 12357, ['A', 'B'])
        trip = trip_service.create_trip(train["id"], train["lines"][0])
        parcel = parcel_service.create_parcel(10, 10)

        booking_service.create_booking(trip["id"], parcel["id"], 200)
        details = TrainAPI.get_train_details(train["id"])
        self.assertEqual(type(details), dict)


class TestParcelAPI(TestCase):

    def test_parcel_api(self):
        a_line = line_service.get_or_create_line('A')
        train = train_service.create_train("train-A", 23, 1265, 12357, [a_line])
        trip = trip_service.create_trip(train["id"], train["lines"][0])
        parcel = ParcelAPI.create_parcel(10, 10)

        booking_service.create_booking(trip["id"], parcel["id"], 200)
        details = ParcelAPI.get_parcel_details(parcel["id"])
        self.assertEqual(type(details), dict)

class PostMasterAPI:

    def test_schedule(self):
        pass

