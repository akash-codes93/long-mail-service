"""
This is the presentation layer
"""

from typing import List

from long_mail_service.service.booking import booking_service
from long_mail_service.service.parcel import parcel_service
from long_mail_service.service.train import train_service
from long_mail_service.service.trip import trip_service
from long_mail_service.service.assignment import assignment_service
from long_mail_service.service.strategy import strategy_manager

trip_service.complete_trips()


class TrainAPI:

    @staticmethod
    def create_train(name: str, cost: int, volume: int, weight: int, lines: List):
        """
        Create train api
        """
        return train_service.create_train(name, cost, volume, weight, lines)

    @staticmethod
    def get_train_details(train_id):
        """
        api to get all the train details + trips + parcels on this train
        """
        train = train_service.get_train(train_id)
        if not train:
            return {
                'message': "Train does not exists"
            }

        trips = trip_service.get_trip_details_using_train_id(train["id"])

        if len(trips) == 0:
            return {
                'train': train,
                'trips': 'Did not scheduled',
            }
        trip_data = []
        for trip in trips:
            bookings = booking_service.get_bookings_from_trip(trip["id"])
            parcels = []
            for booking in bookings:
                parcels.append({
                    'cost': booking["cost"],
                    'id': booking["parcel"]
                })
            trip['parcels'] = parcels
            trip_data.append(trip)

        return {
            'train': train,
            'trips': trip_data,
        }


class ParcelAPI:

    @staticmethod
    def create_parcel(volume: int, weight: int):
        return parcel_service.create_parcel(volume, weight)

    @staticmethod
    def get_parcel_details(parcel_id: id):
        """
        api to get all parcel details
        """
        parcel = parcel_service.get_parcel(parcel_id)
        if not parcel:
            return {
                'message': "Parcel does not exists"
            }

        booking = booking_service.get_booking_from_parcel(parcel_id)
        if not booking:
            return {
                'parcel': parcel["id"],
                'booking': 'Did not booked'
            }

        trip = trip_service.get_trip_details(booking["trip"])

        return {
            'parcel': parcel["id"],
            'booking': booking["id"],
            'cost': booking["cost"],
            'trip': trip
        }


class PostMasterAPI:
    @staticmethod
    def schedule_parcel(strategy_name):

        strategy_class = strategy_manager.map_strategy(strategy_name)()
        return assignment_service(strategy_class).schedule_parcel()

