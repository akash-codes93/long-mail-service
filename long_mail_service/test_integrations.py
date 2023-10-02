"""
Integration test for api and service layer
"""
from django.test import TestCase

from long_mail_service.service.line import line_service
from long_mail_service.api import *


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
        train = train_service.create_train("train-A", 23, 1265, 12357, ["A"])
        trip = trip_service.create_trip(train["id"], train["lines"][0])
        parcel = ParcelAPI.create_parcel(10, 10)

        booking_service.create_booking(trip["id"], parcel["id"], 200)
        details = ParcelAPI.get_parcel_details(parcel["id"])
        self.assertEqual(type(details), dict)


class TestPostMasterAPI(TestCase):

    def test_schedule(self):
        trainA = train_service.create_train("train-A", 20, 50, 100, ["A"])
        trainB = train_service.create_train("train-B", 15, 20, 80, ["A", "B"])
        schedule0 = PostMasterAPI.schedule_parcel()
        # print(schedule0)
        parcelA = ParcelAPI.create_parcel(20, 10)
        parcelB = ParcelAPI.create_parcel(10, 20)
        parcelC = ParcelAPI.create_parcel(5, 10)
        parcelD = ParcelAPI.create_parcel(10, 10)
        parcelE = ParcelAPI.create_parcel(12, 12)
        parcelF = ParcelAPI.create_parcel(12, 12)

        scheduleA = PostMasterAPI.schedule_parcel()
        scheduleB = PostMasterAPI.schedule_parcel()
        # print(scheduleA)
        # print(scheduleB)

        lineC = line_service.get_or_create_line("C")
        scheduleC = PostMasterAPI.schedule_parcel()
        # print(scheduleC)
        trainB = train_service.create_train("train-C", 15, 20, 80, ["B"])
        scheduleD = PostMasterAPI.schedule_parcel()
        # print(scheduleD)

        self.assertEqual(len(scheduleA), 6)
        self.assertEqual(schedule0["message"], "No available parcels. Please add new parcels.")
        self.assertEqual(scheduleB["message"], "No available lines. Please wait till old parcels are delivered.")
        self.assertEqual(scheduleC["message"], "No available trains. Please wait till old parcels are delivered.")
        self.assertEqual(scheduleD["message"], "No available trains-line combination.")

