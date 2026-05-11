import fetch_data
import compare_drugs
import visualize_safety
import side_effect_searcher


def run_pipeline():
    print("🚀 --- PHARMA DATA PIPELINE STARTING --- 🚀\n")

    # The list of drugs
    drugs_to_track = ["Aspirin", "Pembrolizumab", "Vedolizumab"]

    # Step 1: Collect Data
    print("📥 STEP 1: Fetching latest FDA reports...")
    for drug in drugs_to_track:
        fetch_data.fetch_and_archive(drug)

    # Step 2: Analyze & Export to CSV
    print("\n🔬 STEP 2: Analyzing clinical signals & Exporting CSV...")
    compare_drugs.analyze_vault()

    # Step 3: Clinical Signal Detection (The Side Effect Searcher)
    print("\n🩺 STEP 3: Detecting Top 5 Clinical Side Effects...")
    for drug in drugs_to_track:
        side_effect_searcher.find_top_side_effects(drug)

    # Step 4: Visualize
    print("\n📊 STEP 4: Generating Executive Dashboard...")
    visualize_safety.generate_safety_chart()

    print("\n✅ --- PIPELINE EXECUTION COMPLETE ---")


# The trigger to start the program
if __name__ == "__main__":
    run_pipeline()