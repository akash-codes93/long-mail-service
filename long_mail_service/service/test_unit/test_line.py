"""
Unit Test cases related to line service
"""
from django.test import TestCase

from long_mail_service.models import Line
from long_mail_service.service.line import line_service


class TestLineService(TestCase):

    def test_create_line(self):
        line = line_service.get_or_create_line('A')

        exists = True
        try:
            Line.objects.get(id=line["id"])
        except Line.DoesNotExist:
            exists = False

        self.assertEqual(exists, True)

    def test_get_available_lines(self):
        line_service.get_or_create_line('A')
        available_lines = line_service.get_available_lines()

        self.assertEqual(len(available_lines), 1)
