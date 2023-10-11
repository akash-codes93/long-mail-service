import copy
import itertools
from abc import ABC, abstractmethod


class AssignmentStrategy(ABC):

    @abstractmethod
    def assign_strategy(self, available_parcels, available_trains, available_lines, trains):
        pass


class DPAssignmentStrategy(AssignmentStrategy):
    name = "dp"

    def assign_strategy(self, available_parcels, available_trains, available_lines, trains):
        pass


class LinearAssignmentStrategy(AssignmentStrategy):
    name = "Linear"

    def assign_strategy(self, available_parcels, available_trains, available_lines, trains):
        pass


class BTAssignmentStrategy(AssignmentStrategy):
    name = "Backtrack"

    def assign_strategy(self, available_parcels, available_trains, available_lines, trains):

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

        return main_snapshot

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


class StrategyManager():

    @staticmethod
    def map_strategy(strategy_name):
        return {

            "dp": DPAssignmentStrategy,
            "backtrack": BTAssignmentStrategy,
            "linear": LinearAssignmentStrategy

        }.get(strategy_name, BTAssignmentStrategy)


strategy_manager = StrategyManager
