"""
unit testcase for train service
"""
from django.test import TestCase

from long_mail_service.service.train import train_service
from long_mail_service.service.line import line_service
from long_mail_service.service.trip import trip_service


class TestTrainService(TestCase):

    def test_create_train(self):
        train = train_service.create_train("train-A", 23, 1265, 12357, ["A", "B"])
        self.assertEqual(train["name"], "train-A")

    def test_get_available_train(self):
        train = train_service.create_train("train-A", 23, 1265, 12357, ["A", "B"])

        trip_service.create_trip(train["id"], train["lines"][0])

        available_trains = train_service.get_available_trains()
        self.assertEqual(len(available_trains), 0)
