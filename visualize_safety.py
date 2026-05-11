import pandas as pd
import matplotlib.pyplot as plt
import json
import os


def generate_safety_chart():
    vault_path = 'vault'
    drug_names = []
    seriousness_rates = []

    # 1. Extracting data from the vault
    if not os.path.exists(vault_path):
        print("❌ Error: 'vault' folder not found. Run fetch_data.py first!")
        return

    for filename in os.listdir(vault_path):
        if filename.endswith('.json'):
            try:
                with open(os.path.join(vault_path, filename), 'r') as f:
                    data = json.load(f)
                    reports = data.get('results', [])

                    drug_name = filename.replace('raw_', '').replace('.json', '').capitalize()
                    total = len(reports)
                    serious = sum(1 for r in reports if r.get('serious') == '1')

                    rate = (serious / total) * 100 if total > 0 else 0

                    drug_names.append(drug_name)
                    seriousness_rates.append(rate)
            except Exception as e:
                print(f"Skipping {filename} due to error: {e}")

    # 2. CREATING THE CHART
    if not drug_names:
        print("❌ No data found in vault to visualize.")
        return

    plt.figure(figsize=(10, 6))
    # Use professional colors: Blue for lower risk, Red/Orange for higher risk
    colors = ['#3498db' if r < 70 else '#e67e22' for r in seriousness_rates]
    bars = plt.bar(drug_names, seriousness_rates, color=colors)

    # 3. Add Labels & Styling
    plt.title('FDA Safety Signal Comparison: Seriousness Rate (%)', fontsize=14, fontweight='bold')
    plt.ylabel('Percentage of Reports Marked "Serious"', fontsize=12)
    plt.ylim(0, 100)

    # Adding the percentage numbers on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 1,
                 f'{round(height, 1)}%', ha='center', va='bottom', fontweight='bold')

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    print("📊 Generating chart... look for the popup window!")
    plt.show()

    #trigger
if __name__ == "__main__":
    generate_safety_chart()