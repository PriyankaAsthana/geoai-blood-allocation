import matplotlib.pyplot as plt
from config import GRID_SIZE

# ==============================
# Plot Spatial Distribution
# ==============================

def plot_environment(banks, requests, save_path="outputs_spatial_distribution.png"):
    
    bank_x = [b["x"] for b in banks]
    bank_y = [b["y"] for b in banks]

    request_x = [r["x"] for r in requests]
    request_y = [r["y"] for r in requests]

    plt.figure(figsize=(8, 8))
    
    # Plot requests
    plt.scatter(request_x, request_y, 
                color="lightgray", 
                s=10, 
                alpha=0.6, 
                label="Emergency Requests")

    # Plot banks
    plt.scatter(bank_x, bank_y, 
                color="red", 
                s=80, 
                marker="^", 
                label="Blood Banks")

    plt.xlim(0, GRID_SIZE)
    plt.ylim(0, GRID_SIZE)

    plt.title("Spatial Distribution of Blood Banks and Emergency Requests")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()

    plt.grid(True, linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

    print(f"Figure saved as: {save_path}")
