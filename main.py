from environment import generate_blood_banks, generate_requests
from visualization import plot_environment

# Generate world
banks = generate_blood_banks()
requests = generate_requests()

print("=== Simulation Environment Created ===")
print(f"Total Blood Banks: {len(banks)}")
print(f"Total Emergency Requests: {len(requests)}")

# Plot spatial environment
plot_environment(banks, requests)
