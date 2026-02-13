import matplotlib.pyplot as plt
import os

def plot_results(success, failed):

    labels = ["Successful", "Failed"]
    values = [success, failed]

    plt.figure()
    plt.bar(labels, values)

    plt.title("Token Allocation Performance")

    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/token_performance.png", dpi=300)

    plt.show()
