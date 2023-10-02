from typing import List, Dict

from long_mail_service.models import Train, Trip
from long_mail_service.service.line import line_service
from long_mail_service.service.serializers import TrainSerializer


class TrainService:

    @staticmethod
    def create_train(name: str, cost: int, volume: int, weight: int, lines: List) -> Dict:
        """
        Create trains with given details
        """
        line_objs = [line_service.get_or_create_line(line) for line in lines]

        train = Train.objects.create(name=name, cost=cost, volume=volume, weight=weight)
        train.save()

        for line in line_objs:
            train.lines.add(line["id"])

        return TrainSerializer(train).data

    @staticmethod
    def get_available_trains() -> List:
        """
        Get all the trains available to service parcels
        """
        busy_trains = Trip.objects.filter(is_completed=False).values_list('train_id', flat=True)
        available_trains = Train.objects.exclude(id__in=busy_trains)

        return TrainSerializer(available_trains, many=Train).data

    @staticmethod
    def get_train(train_id: int):
        """
        Get details of trains using booking
        input
        train_id: int
        """
        try:
            train = Train.objects.get(id=train_id)
            return TrainSerializer(train).data
        except Train.DoesNotExist:
            return None


train_service = TrainService()
