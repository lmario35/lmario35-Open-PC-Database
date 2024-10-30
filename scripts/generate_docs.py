import os
import json

def generate_md_from_schema(schema_path, output_path):
    with open(schema_path, 'r') as schema_file:
        schema = json.load(schema_file)

    lines = [
        f"# {schema.get('title', 'Component Schema')}\n",
        f"{schema.get('description', 'No description available.')}\n",
        "## Properties\n"
    ]

    properties = schema.get('properties', {})
    for prop, details in properties.items():
        lines.append(f"### {prop}\n")
        lines.append(f"- **Type**: {details.get('type', 'unknown')}\n")
        lines.append(f"- **Description**: {details.get('description', 'No description available.')}\n")
        if 'enum' in details:
            lines.append(f"- **Allowed Values**: {', '.join(details['enum'])}\n")

    with open(output_path, 'w') as md_file:
        md_file.writelines("\n".join(lines))

def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith("_schema.json"):
                schema_path = os.path.join(root, file)
                output_path = schema_path.replace("_schema.json", ".md")
                generate_md_from_schema(schema_path, output_path)
                print(f"Generated documentation for {schema_path} -> {output_path}")

if __name__ == "__main__":
    main()
