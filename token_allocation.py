import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def run_token_allocation(banks, requests):

    banks = copy.deepcopy(banks)

    success = 0
    failed = 0
    total_distance = 0

    priority_weight = {"high": 0.6, "medium": 1.0, "low": 1.4}

    for req in requests:

        req_point = (req["x"], req["y"])
        best_bank = None
        best_score = float("inf")
        best_distance = 0

        for bank in banks:

            if bank["inventory"] > 0:

                bank_point = (bank["x"], bank["y"])
                d = distance(req_point, bank_point)

                # 🔥 REAL GEOAI LOGIC

                # 1. Priority-weighted distance
                weighted_distance = d * priority_weight[req["priority"]]

                # 2. Load balancing term
                load_penalty = (1 / (bank["inventory"] + 1)) * 50

                # 3. Served count smoothing
                served = bank.get("served", 0)
                congestion_penalty = served * 0.2

                score = weighted_distance + load_penalty + congestion_penalty

                if score < best_score:
                    best_score = score
                    best_bank = bank
                    best_distance = d

        if best_bank:

            best_bank["inventory"] -= 1
            best_bank["served"] = best_bank.get("served", 0) + 1

            success += 1
            total_distance += best_distance

        else:
            failed += 1

    return {
        "success_rate": success / len(requests),
        "avg_distance": total_distance / success if success > 0 else 0
    }
