import matplotlib.pyplot as plt
import os

def plot_comparison(baseline, token):

    models = ["Baseline", "Token"]
    success_rates = [baseline["success_rate"], token["success_rate"]]
    avg_distances = [baseline["avg_distance"], token["avg_distance"]]

    plt.figure()
    plt.bar(models, success_rates)
    plt.title("Success Rate Comparison")
    plt.ylabel("Success Rate")

    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/success_rate_comparison.png", dpi=300)
    plt.show()

    plt.figure()
    plt.bar(models, avg_distances)
    plt.title("Average Distance Comparison")
    plt.ylabel("Average Distance")

    plt.savefig("outputs/avg_distance_comparison.png", dpi=300)
    plt.show()
