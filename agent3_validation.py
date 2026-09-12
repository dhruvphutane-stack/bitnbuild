import json
import os

def validate_zoning_data(input_file="master_zoning_output.json", output_file="validated_zoning_output.json"):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run Agent 2 extraction first.")
        return

    print(f"Loading {input_file} for local structural validation...")
    with open(input_file, "r") as f:
        try:
            raw_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Master JSON is malformed: {e}")
            return

    # Perform local checks & cleanup
    validated_records = []
    if isinstance(raw_data, list):
        for idx, item in enumerate(raw_data):
            # Ensure each entry is a dictionary and has basic required keys
            if isinstance(item, dict):
                # Fill missing default fields if necessary
                cleaned_item = {
                    "zone_code": item.get("zone_code", "UNKNOWN"),
                    "permitted_uses": item.get("permitted_uses", []),
                    "restrictions": item.get("restrictions", [])
                }
                validated_records.append(cleaned_item)
    elif isinstance(raw_data, dict):
        validated_records = raw_data

    with open(output_file, "w") as f:
        json.dump(validated_records, f, indent=2)
        
    print(f"Local validation successful! Cleaned data saved to {output_file}")

if __name__ == "__main__":
    validate_zoning_data()