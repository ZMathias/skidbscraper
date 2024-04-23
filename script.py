import json

# Load the data from the JSON file
with open('resort-links.json') as f:
    data = json.load(f)

# Open a new file to write the links
with open('links.txt', 'w') as f:
    # Iterate through the top-level list
    for item in data:
        # Check if the item is a dictionary
        if isinstance(item, dict):
            # Iterate through the fields in the dictionary
            for field in item:
                # Check if the field value is a list
                if isinstance(item[field], list):
                    # Iterate through the links in the field
                    for link in item[field]:
                        # Write each link to a new line in the file
                        f.write(f'{link}\n')
                elif isinstance(item[field], str) and 'http' in item[field]:
                    f.write(f'{item[field]}\n')