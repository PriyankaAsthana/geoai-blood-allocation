import numpy as np
from environment import generate_blood_banks, generate_requests
from allocation import run_baseline_allocation, run_token_allocation

def run_multiple_simulations(runs=30, demand=800):

    baseline_success = []
    token_success = []

    baseline_distance = []
    token_distance = []

    for _ in range(runs):

        banks = generate_blood_banks()
        requests = generate_requests(demand)

        base = run_baseline_allocation(banks, requests)
        token = run_token_allocation(banks, requests)

        baseline_success.append(base["success_rate"])
        token_success.append(token["success_rate"])

        baseline_distance.append(base["avg_distance"])
        token_distance.append(token["avg_distance"])

    return {
        "baseline_avg": np.mean(baseline_success),
        "token_avg": np.mean(token_success),
        "baseline_std": np.std(baseline_success),
        "token_std": np.std(token_success),
        "baseline_distance": np.mean(baseline_distance),
        "token_distance": np.mean(token_distance)
    }
