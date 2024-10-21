import csv
with open('gen1.csv', 'r') as csvfile:
    pokereader = csv.DictReader(csvfile, delimiter=' ')
    scrubbed_data = []
    for row in pokereader:
        # Example scrubbing: filter out rows where a specific field is empty
        if row['Type1']:  # Replace 'important_field' with your field name
            # You can transform or extract data here
            scrubbed_row = {
                'Type1': row['Type1'],  # Replace with actual fields you want to keep
            }
            print(scrubbed_data.append(scrubbed_row))