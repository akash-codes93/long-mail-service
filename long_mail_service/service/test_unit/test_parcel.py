"""
Unit Test cases related to parcel service
"""

from django.test import TestCase

from long_mail_service.models import Parcel
from long_mail_service.service.parcel import parcel_service


class TestParcelService(TestCase):

    def test_create_parcel(self):
        parcel = parcel_service.create_parcel(10, 10)

        exists = True
        try:
            Parcel.objects.get(id=parcel["id"])
        except Parcel.DoesNotExist:
            exists = False

        self.assertEqual(exists, True)

    def test_get_parcel_details(self):
        parcel = parcel_service.create_parcel(10, 10)
        parcel_details = parcel_service.get_parcel(parcel["id"])
        parcel_dne = parcel_service.get_parcel(5000)
        self.assertEqual(parcel, parcel_details)
        self.assertEqual(parcel_dne, None)
