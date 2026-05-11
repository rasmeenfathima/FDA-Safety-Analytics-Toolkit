# FDA Adverse Event Analytics Pipeline (v1.0)

## Overview
This Python-based toolkit automates the extraction and analysis of drug safety data from the FDA openFDA API. It is designed to assist clinical consultants in identifying safety signals and comparing seriousness rates across different therapeutic agents.

## Key Features
*   **Automated Data Retrieval:** Fetches raw JSON records directly from FDA databases.
*   **Clinical Signal Detection:** Uses MedDRA preferred terms to identify the top 5 most frequent adverse reactions.
*   **Statistical Analysis:** Calculates seriousness ratios to benchmark drug safety profiles.
*   **Data Visualization:** Generates comparative bar charts for executive-level reporting.
*   **Export Capabilities:** Outputs processed data to CSV for further integration with Excel or Tableau.

## Technical Architecture
The system is modularized into five core components:
1. `fetch_data`: Handles API connectivity and local archiving.
2. `compare_drugs`: Logic engine for safety metric calculations.
3. `side_effect_searcher`: MedDRA term frequency analyzer.
4. `visualize_safety`: Matplotlib-based dashboard generator.
5. `main`: The orchestration layer for the full pipeline.

