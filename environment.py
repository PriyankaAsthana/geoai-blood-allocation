import random

GRID_SIZE = 100

def generate_blood_banks(num_banks=20):

    banks = []

    for _ in range(num_banks):

        # Create uneven inventory distribution
        banks.append({
            "x": random.randint(0, GRID_SIZE),
            "y": random.randint(0, GRID_SIZE),
            "inventory": random.choice(
                [random.randint(10, 20), random.randint(30, 60)]
            )
        })

    return banks


def generate_requests(demand=500):

    requests = []

    # Create 2 demand clusters
    cluster_centers = [(30, 30), (75, 75)]

    for _ in range(demand):

        if random.random() < 0.7:  # 70% clustered demand
            cx, cy = random.choice(cluster_centers)
            x = int(random.gauss(cx, 10))
            y = int(random.gauss(cy, 10))
        else:
            x = random.randint(0, GRID_SIZE)
            y = random.randint(0, GRID_SIZE)

        requests.append({
            "x": max(0, min(GRID_SIZE, x)),
            "y": max(0, min(GRID_SIZE, y)),
            "priority": random.choices(
                ["high", "medium", "low"],
                weights=[0.3, 0.4, 0.3]
            )[0]
        })

    return requests
