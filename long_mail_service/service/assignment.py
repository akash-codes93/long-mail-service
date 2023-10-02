import copy
import itertools
from collections import defaultdict

from long_mail_service.service.booking import booking_service
from long_mail_service.service.line import line_service
from long_mail_service.service.parcel import parcel_service
from long_mail_service.service.train import train_service
from long_mail_service.service.trip import trip_service


class TrainLineDto:

    def __init__(self, train, line):
        self.train = train
        self.line = line


class AssignmentService:

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

        # finding all combination of trains and lines
        permutations = itertools.permutations(trains, len(available_lines))
        unique_comb = []

        for comb in permutations:
            combs = zip(comb, available_lines)
            # print(list(combs))
            # filtering out the invalid combinations - as train and line can be a miss match
            valid_comb = []
            for each_comb in combs:
                train = dict(each_comb[0])
                train["parcels"] = []
                line = each_comb[1]

                if line in train['lines']:
                    valid_comb.append({
                        **dict(train),
                        "line": line
                    })
            if valid_comb:
                unique_comb.append(valid_comb)

        # print(unique_comb)
        main_snapshot = available_parcels
        main_cost = float('inf')
        main_count = 0
        for comb in unique_comb:
            snapshot, count, cost = self.find_parcels_and_cost(comb, available_parcels)
            # print("out", snapshot, count, cost)
            if count >= main_count:
                if cost < main_cost:
                    main_snapshot = copy.deepcopy(snapshot)
                    main_cost = cost
                    main_count = count

        # print(main_snapshot, main_cost, main_count)

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
        self.create_trips_and_bookings(train_scheduled)

        return schedule

    @staticmethod
    def create_trips_and_bookings(train_scheduled):
        for train_id, line_id in train_scheduled:
            # create trip only if parcels are present
            if len(train_scheduled[(train_id, line_id)]) > 0:
                trip_id = trip_service.create_trip(train_id, line_id)["id"]
                # create bookings
                for parcel_id, cost in train_scheduled[(train_id, line_id)]:
                    booking_service.create_booking(trip_id, parcel_id, cost)

    @staticmethod
    def find_parcels_and_cost(trains, parcels):
        """
        backtracking approach;;could use some linear programming algo using PuLP
        """

        min_cost = [float('inf')]
        parcels_scheduled = [0]
        snapshot = [None]

        def dfs(j, count, cost):
            if j == len(parcels):
                if count >= parcels_scheduled[0]:
                    if cost < min_cost[0]:
                        min_cost[0] = cost
                        parcels_scheduled[0] = count
                        snapshot[0] = copy.deepcopy(parcels)
                return

            parcel = parcels[j]

            for option in ["schedule", "unschedule"]:
                if option == "schedule":
                    for train in trains:
                        if train["weight"] >= parcel["weight"] and train["volume"] >= parcel["volume"]:
                            train["weight"] -= parcel["weight"]
                            train["volume"] -= parcel["volume"]
                            _cost = (train['unit_cost']) * (parcel["weight"] / parcel["volume"])

                            parcel["cost"] = _cost
                            parcel["train_id"] = train["id"]
                            parcel["line_id"] = train["line"]

                            dfs(j + 1, count + 1, cost + _cost)

                            train["weight"] += parcel["weight"]
                            train["volume"] += parcel["volume"]
                            parcel.pop('train_id')
                            parcel.pop('cost')
                            parcel.pop('line_id')
                else:
                    dfs(j + 1, count, cost)

        dfs(0, 0, 0)
        return snapshot[0], parcels_scheduled[0], min_cost[0]


assignment_service = AssignmentService()
