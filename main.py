from experiments import run_multiple_simulations
from visualization import plot_model_comparison, plot_distance_comparison

print("Running GeoAI Stability Experiment...")

results = run_multiple_simulations(runs=40, demand=2000)

print("\n=== Results ===")
print(f"Baseline Success: {results['baseline_avg']:.4f}")
print(f"GeoAI Success: {results['token_avg']:.4f}")

plot_model_comparison(results)
plot_distance_comparison(results)

print("\nPlots saved in outputs folder.")
