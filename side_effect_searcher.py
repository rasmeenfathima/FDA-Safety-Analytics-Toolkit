import os
import json
from collections import Counter


def find_top_side_effects(drug_name):

    filename = f"vault/raw_{drug_name.capitalize()}.json"

    if not os.path.exists(filename):
        return

    with open(filename, 'r') as f:
        data = json.load(f)
        reports = data.get('results', [])

    reactions = []
    for r in reports:
        if 'patient' in r and 'reaction' in r['patient']:
            for reaction in r['patient']['reaction']:
                term = reaction.get('reactionmeddrapt', 'Unknown')
                reactions.append(term.upper())
    # Frequency-based ranking to highlight potential safety signals for medical review
    counts = Counter(reactions).most_common(5)

    print(f"🩺 TOP SIGNALS FOR {drug_name.upper()}:")
    for term, count in counts:
        print(f"   - {term}: {count} cases")