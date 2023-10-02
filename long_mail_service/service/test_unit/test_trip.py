"""
unit test case trip service
"""
import time
from django.test import TestCase

from long_mail_service.service.train import train_service
from long_mail_service.service.trip import trip_service


class TestTripService(TestCase):

    def test_complete_trip(self):

        train = train_service.create_train("train-A", 23, 1265, 12357, ["A", "B"])

        trip = trip_service.create_trip(train["id"], train["lines"][0])
        time.sleep(1)
        trip_service.complete_trips(0.000000001)

        details = trip_service.get_trip_details_using_train_id(trip["id"])
        trip_details = trip_service.get_trip_details(trip["id"])
        self.assertEqual(details[0]["is_completed"], True)
        self.assertEqual(details[0]["id"], trip_details["id"])

