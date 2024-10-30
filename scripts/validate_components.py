import json
import os
import sys
from jsonschema import validate, ValidationError

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def validate_data(schema_path, data_path):
    try:
        schema = load_json(schema_path)
        data = load_json(data_path)

        for component in data.get("components", []):
            validate(instance=component, schema=schema)
        print(f"Validation successful for {data_path}")
    except ValidationError as e:
        print(f"Validation error in {data_path}: {e.message}")
        sys.exit(1)  # Exit with code 1 if validation fails
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)  # Exit with code 1 for any unexpected errors

def main():
    components = ["cpu", "gpu", "ram"]
    has_errors = False

    for component in components:
        schema_path = f"{component}/{component}_schema.json"
        data_path = f"{component}/{component}.json"

        if os.path.exists(schema_path) and os.path.exists(data_path):
            try:
                validate_data(schema_path, data_path)
            except SystemExit:
                has_errors = True
        else:
            print(f"Schema or data file missing for {component}")
            has_errors = True

    if has_errors:
        sys.exit(1)

if __name__ == "__main__":
    main()
