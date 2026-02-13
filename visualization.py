import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

def plot_model_comparison(results):

    models = ["GeoAI Token", "Baseline"]
    means = [results["baseline_avg"], results["token_avg"]]
    stds = [results["baseline_std"], results["token_std"]]

    plt.figure(figsize=(7,5))
    bars = plt.bar(models, means, yerr=stds, capsize=10)

    bars[0].set_color("gray")
    bars[1].set_color("green")

    plt.ylabel("Success Rate")
    plt.title("GeoAI Outperforms Baseline Under Demand Clustering")
    plt.ylim(0, 1)

    plt.savefig("outputs/model_comparison.png")
    plt.close()


def plot_distance_comparison(results):

    models = ["Baseline", "GeoAI Token"]
    values = [results["baseline_distance"], results["token_distance"]]

    plt.figure(figsize=(7,5))
    bars = plt.bar(models, values)

    bars[0].set_color("gray")
    bars[1].set_color("green")

    plt.ylabel("Average Allocation Distance")
    plt.title("Average Distance Comparison")

    plt.savefig("outputs/distance_comparison.png")
    plt.close()
