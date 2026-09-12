import os
import json
import time
from agent1_ingestion import extract_text_from_pdf
from agent2_extraction import run_agent_2

def run_pipeline():
    pdf_file = "bda_rmp_2031.pdf"

    print("Running Agent 1: Extracting and chunking PDF text...")
    chunks = extract_text_from_pdf(pdf_file)
    print(f"Generated {len(chunks)} chunks.")

    master_results = []

    print("Running Agent 2 on the first 3 chunks...")
    for idx, chunk in enumerate(chunks[:19]):
        print(f"Processing chunk {idx + 1}/3...")
        try:
            result = run_agent_2(chunk)
            master_results.append(result)
            time.sleep(2)
        except Exception as e:
            print(f"Error on chunk {idx + 1}: {e}")

    output_file = "master_zoning_output.json"
    with open(output_file, "w") as f:
        json.dump(master_results, f, indent=2)

    print(f"Pipeline complete! Saved output to {output_file}")

if __name__ == "__main__":
    run_pipeline()