import os
import requests
import json


def fetch_and_archive(drug_name):

    if not os.path.exists('vault'):
        os.makedirs('vault')

    # Fetching the data from the FDA
    url = f"https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:{drug_name}&limit=100"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # This saves the file inside the vault with its own name
        file_path = f"vault/raw_{drug_name}.json"

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"✅ {drug_name} is now safely in the vault.")


# Running the archiver for both drugs
fetch_and_archive("Aspirin")
fetch_and_archive("Pembrolizumab")
