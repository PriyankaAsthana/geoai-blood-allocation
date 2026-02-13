import math
import copy


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# =========================
# BASELINE MODEL
# =========================

def run_baseline_allocation(banks, requests):

    banks = copy.deepcopy(banks)

    success = 0
    failed = 0
    total_distance = 0

    for req in requests:

        req_point = (req["x"], req["y"])
        nearest_bank = None
        min_dist = float("inf")

        for bank in banks:
            if bank["inventory"] > 0:
                bank_point = (bank["x"], bank["y"])
                d = distance(req_point, bank_point)

                if d < min_dist:
                    min_dist = d
                    nearest_bank = bank

        if nearest_bank:
            nearest_bank["inventory"] -= 1
            success += 1
            total_distance += min_dist
        else:
            failed += 1

    return {
        "success_rate": success / len(requests),
        "avg_distance": total_distance / success if success > 0 else 0
    }


# =========================
# GEOAI TOKEN MODEL
# =========================

def run_token_allocation(banks, requests):

    banks = copy.deepcopy(banks)

    success = 0
    failed = 0
    total_distance = 0

    # sort by priority (high first)
    priority_order = {"high": 0, "medium": 1, "low": 2}
    requests_sorted = sorted(requests, key=lambda r: priority_order[r["priority"]])

    for req in requests_sorted:

        req_point = (req["x"], req["y"])

        best_bank = None
        best_score = float("inf")

        for bank in banks:
            if bank["inventory"] > 0:

                bank_point = (bank["x"], bank["y"])
                d = distance(req_point, bank_point)

                # predictive protection: keep minimum stock buffer
                buffer = 5

                if bank["inventory"] <= buffer:
                    continue

                # geoai scoring: distance + inverse inventory
                score = d * 0.7 + (1 / bank["inventory"]) * 30

                if score < best_score:
                    best_score = score
                    best_bank = bank

        if best_bank:
            best_bank["inventory"] -= 1
            success += 1
            total_distance += distance(req_point, (best_bank["x"], best_bank["y"]))
        else:
            failed += 1

    return {
        "success_rate": success / len(requests),
        "avg_distance": total_distance / success if success > 0 else 0
    }
