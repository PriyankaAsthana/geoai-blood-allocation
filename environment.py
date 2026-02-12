import random
from config import *

# ==============================
# Blood Bank Generator
# ==============================

def generate_blood_banks():
    banks = []

    for i in range(NUM_BANKS):
        bank = {
            "id": i,
            "x": random.uniform(0, GRID_SIZE),
            "y": random.uniform(0, GRID_SIZE),
            "inventory": {
                blood_type: random.randint(MIN_UNITS_PER_TYPE, MAX_UNITS_PER_TYPE)
                for blood_type in BLOOD_TYPES
            }
        }
        banks.append(bank)

    return banks


# ==============================
# Emergency Request Generator
# ==============================

def generate_requests():
    requests = []

    for i in range(NUM_REQUESTS):
        request = {
            "id": i,
            "x": random.uniform(0, GRID_SIZE),
            "y": random.uniform(0, GRID_SIZE),
            "blood_type": random.choice(BLOOD_TYPES)
        }
        requests.append(request)

    return requests
