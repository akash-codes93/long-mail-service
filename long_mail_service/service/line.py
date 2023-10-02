from typing import List, Dict

from long_mail_service.models import Line, Trip
from long_mail_service.service.serializers import LineSerializer


class LineService:

    @staticmethod
    def get_or_create_line(name: str) -> Dict:
        """
        Create a line
        name: name of line

        return: int
        id: id of line created
        """
        try:
            line = Line.objects.get(name=name)
        except Line.DoesNotExist:
            line = Line.objects.create(name=name)
            line.save()
        return LineSerializer(line).data

    @staticmethod
    def get_available_lines() -> List:
        """
        all the line that are free to run trains
        return list
        """
        busy_lines = Trip.objects.filter(is_completed=False).values_list('train_id', flat=True)
        available_lines = Line.objects.exclude(id__in=busy_lines)

        return LineSerializer(available_lines, many=True).data


line_service = LineService()
