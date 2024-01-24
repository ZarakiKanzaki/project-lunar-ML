import os
import csv
import json
import argparse

def parse_cards(file_path):
    """Parse cards from a JSON file and simplify the data."""
    with open(file_path, 'r', encoding='utf-8') as file:
        cards = json.load(file)

    simplified_cards = {}
    for card in cards:
        attributes = {
            "mana_cost": card.get("mana_cost", ""),
            "type_line": card.get("type_line", ""),
            "oracle_text": card.get("oracle_text", "")
        }
        # Add power, toughness, and loyalty if present
        for attr in ["power", "toughness", "loyalty"]:
            if attr in card:
                attributes[attr] = card[attr]

        simplified_cards[card["name"]] = attributes

    return simplified_cards

def load_json_data(json_file_path):
    """Load JSON data from a file."""
    with open(json_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def format_json_for_csv(card_name, json_data):
    """Format JSON data for CSV output."""
    json_data_with_name = {"name": card_name, **json_data}
    formatted_string = json.dumps(json_data_with_name).replace('\n', '\\n')
    return formatted_string

def extract_card_name(content):
    """Extract card name from content."""
    for line in content.split('\n'):
        if line.startswith("Name:"):
            return line.split(':', 1)[1].strip()
    return None

def write_data_to_csv(data, file_name):
    """Write extracted data to a CSV file."""
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['instruction', 'input', 'output', 'text'])
        for name, json_input, content in data:
            formatted_content = content.replace('\n', '\\n')
            combined_text = (f"Below is an instruction that describes a task then the input and response.\n"
                             f"### Instruction: Create the Forge script for this magic card\n"
                             f"### Input: {json_input}\n"
                             f"### Response: {formatted_content}")
            writer.writerow(["Create the Forge script for this magic card", json_input, formatted_content, combined_text])

def extract_data_from_files(base_path, json_data):
    """Extract and combine data from files and JSON."""
    all_data = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().strip()
                        card_name = extract_card_name(content)
                        if card_name:
                            json_input = json_data.get(card_name, {})
                            formatted_json_input = format_json_for_csv(card_name, json_input)
                            all_data.append((card_name, formatted_json_input, content))
                except UnicodeDecodeError as e:
                    print(f"Error reading file {file_path}: {e}")
                    continue
    return all_data

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(description='Process card files and generate CSV.')
    parser.add_argument('scryfall_batch_oracle_json', help='Path to the scryfall batch oracle JSON file with card details.')
    parser.add_argument('forge_cardsfolder_base_path', help='Base path for the Forge cardsfolder files.')
    parser.add_argument('output_csv_path', help='Path for the output CSV file ready to train an LLM e.g. llama2 with autotrain.')
    args = parser.parse_args()

    # Parse and simplify cards
    simplified_cards = parse_cards(args.scryfall_batch_oracle_json)

    # Extract and compile data
    compiled_data = extract_data_from_files(args.forge_cardsfolder_base_path, simplified_cards)

    # Write the data to a CSV file
    write_data_to_csv(compiled_data, args.output_csv_path)
    print(f"Created CSV file: {args.output_csv_path}")

if __name__ == "__main__":
    main()
