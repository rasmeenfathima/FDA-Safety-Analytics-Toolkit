import os
import json
import csv


def analyze_vault():
    vault_path = 'vault'
    all_summaries = []

    if not os.path.exists(vault_path):
        print("Vault not found.")
        return

    print(f"{'Drug Name':<20} | {'Total':<8} | {'Serious':<8} | {'Rate':<6}")
    print("-" * 50)

    for filename in os.listdir(vault_path):
        if filename.endswith('.json'):
            with open(os.path.join(vault_path, filename), 'r') as f:
                data = json.load(f)
                reports = data.get('results', [])

                drug_name = filename.replace('raw_', '').replace('.json', '').capitalize()
                total = len(reports)
                serious = sum(1 for r in reports if r.get('serious') == '1')
                rate = (serious / total) * 100 if total > 0 else 0

                print(f"{drug_name:<20} | {total:<8} | {serious:<8} | {rate:>5.1f}%")

                #  this is for storing data for the CSV
                all_summaries.append({
                    "Drug": drug_name,
                    "Total_Reports": total,
                    "Serious_Reports": serious,
                    "Seriousness_Rate": f"{rate:.1f}%"
                })

    # this is exporting to csv
    keys = all_summaries[0].keys()
    with open('safety_report_export.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_summaries)

    print(f"\n📁 Exported safety data to: safety_report_export.csv")


if __name__ == "__main__":
    analyze_vault()