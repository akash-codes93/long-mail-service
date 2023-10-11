from django.test import TestCase

from unittest.mock import patch

from long_mail_service.service.train import train_service
from long_mail_service.service.parcel import parcel_service
from long_mail_service.service.booking import booking_service
from long_mail_service.service.assignment import assignment_service, strategy_manager


class TestAssignment(TestCase):

    def test_bt_assignment_strategy(self):
        trainA = train_service.create_train("train-A", 100, 200, 500, ["A"])
        trainB = train_service.create_train("train-B", 50, 100, 1000, ["A", "B"])
        # print(schedule0)

        parcelA = parcel_service.create_parcel(20, 50)
        parcelB = parcel_service.create_parcel(50, 70)
        parcelC = parcel_service.create_parcel(100, 100)

        strategy = strategy_manager.map_strategy("backtrack")

        assignment_service(strategy).schedule_parcel()

        booking = booking_service.get_booking_from_parcel(parcelA["id"])

        self.assertEqual('Backtrack', booking["strategy"])
