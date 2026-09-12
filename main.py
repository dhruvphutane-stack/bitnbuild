import os
import json
import time
from agent1_ingestion import extract_text_from_pdf
from agent2_extraction import run_agent_2
from agent3_validation import validate_zoning_data
import agent4_interface

def run_pipeline():
    pdf_file = "bda_rmp_2031.pdf"
    output_file = "master_zoning_output.json"

    print("Running Agent 1: Extracting and chunking PDF text...")
    chunks = extract_text_from_pdf(pdf_file)
    print(f"Generated {len(chunks)} chunks.")

    master_results = []

    print("Running Agent 2 on the first 3 chunks...")
    for idx, chunk in enumerate(chunks[:3]):
        print(f"Processing chunk {idx + 1}/3...")
        try:
            result = run_agent_2(chunk)
            if result:
                master_results.append(result)
            time.sleep(2)
        except Exception as e:
            print(f"Error processing chunk {idx + 1}/{len(chunks)}: {e}")

    # Preserve existing file if API failed to extract new chunks
    if master_results:
        with open(output_file, "w") as f:
            json.dump(master_results, f, indent=2)
        print(f"Pipeline complete! Saved output to {output_file}")
    else:
        print(f"\n[Warning] API rate limit hit. Preserving pre-existing {output_file} for execution.")

    print("\nRunning Agent 3 Validation...")
    validate_zoning_data()

    print("\n--- Running Agent 4: Query Interface ---")
    agent4_interface.query_civiclens("Floor Area Ratio")

if __name__ == "__main__":
    run_pipeline()