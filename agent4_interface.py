import json
import os

def query_civiclens(search_term, input_file="master_zoning_output.json"):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    print(f"CivicLens Agent 4: Searching {input_file} for '{search_term}'...\n")
    with open(input_file, "r") as f:
        data = json.load(f)

    data_str = json.dumps(data).lower()
    if search_term.lower() not in data_str:
        print(f"No records found matching '{search_term}'.")
        return

    print(f"Match found for '{search_term}'!\n")
    
    items = data if isinstance(data, list) else [data]
    for idx, item in enumerate(items, 1):
        if search_term.lower() in json.dumps(item).lower():
            print(f"--- Result {idx} ---")
            output = json.dumps(item, indent=2)
            print(output)

if __name__ == "__main__":
    query_civiclens("Floor Area Ratio")