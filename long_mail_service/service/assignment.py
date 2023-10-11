from collections import defaultdict

from long_mail_service.service.booking import booking_service
from long_mail_service.service.line import line_service
from long_mail_service.service.parcel import parcel_service
from long_mail_service.service.train import train_service
from long_mail_service.service.trip import trip_service
from long_mail_service.service.strategy import AssignmentStrategy



class AssignmentService:

    def __init__(self, strategy: AssignmentStrategy):
        self.strategy = strategy

    def schedule_parcel(self):
        """
        This method is used to create schedule for trains, line and parcels.
        returns schedule and saves to database
        """

        available_trains = train_service.get_available_trains()
        available_lines = [line["id"] for line in line_service.get_available_lines()]
        available_parcels = [dict(parcel) for parcel in parcel_service.get_available_parcels()]
        # print(available_trains, available_lines, available_parcels)

        if len(available_lines) == 0:
            return {
                "message": "No available lines. Please wait till old parcels are delivered."
            }
        elif len(available_parcels) == 0:
            return {
                "message": "No available parcels. Please add new parcels."
            }
        elif len(available_trains) == 0:
            return {
                "message": "No available trains. Please wait till old parcels are delivered."
            }

        trains = []

        for train in available_trains:
            train_data = train
            lines_present = []
            for line in train["lines"]:
                if line in available_lines:
                    lines_present.append(line)
            if lines_present:
                train_data["lines"] = lines_present
                trains.append(train)

        if not trains:
            return {
                "message": "No available trains-line combination."
            }

        # assignment strategy
        main_snapshot = self.strategy.assign_strategy(available_parcels, available_trains, available_lines, trains)

        # preparing return data
        schedule = []
        train_scheduled = defaultdict(list)
        for sn in main_snapshot:
            d = {
                "parcel_id": sn["id"],
                "train_id": sn["train_id"] if "train_id" in sn else None,
                "cost": sn["cost"] if "cost" in sn else None,
                "line_id": sn["line_id"] if "line_id" in sn else None
            }
            schedule.append(d)
            if d["train_id"]:
                train_scheduled[(d["train_id"], d["line_id"])].append((d["parcel_id"], d["cost"]))
            else:
                d.update({
                    "message": "Parcel did not schedule due to optimisation in this run. Please wait for next schedule."
                })

        # saving schedule in db
        # print(train_scheduled)
        self.create_trips_and_bookings(train_scheduled, self.strategy.name)

        return schedule

    @staticmethod
    def create_trips_and_bookings(train_scheduled, strategy_name):
        for train_id, line_id in train_scheduled:
            # create trip only if parcels are present
            if len(train_scheduled[(train_id, line_id)]) > 0:
                trip_id = trip_service.create_trip(train_id, line_id)["id"]
                # create bookings
                for parcel_id, cost in train_scheduled[(train_id, line_id)]:
                    booking_service.create_booking(trip_id, parcel_id, cost, strategy_name)


assignment_service = AssignmentService
