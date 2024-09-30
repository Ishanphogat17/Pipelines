import os
import csv

# Define the directory containing the text files and the output CSV file path
input_directory = r'C:\Users\Ishan\Downloads\files\files'  # Directory with text files
output_file = r'C:\Users\Ishan\Downloads\files\files\output.csv'  # Path to save the CSV file

# Initialize an empty list to store the data
data_list = []

# Iterate through each file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):  # Process only .txt files
        file_path = os.path.join(input_directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file
            content = file.read().strip()
            # Replace any newlines in the content with space to keep it on one line
            content = content.replace('\n', ' ').replace('\r', '')
            # Append the filename and content to the data list
            data_list.append([filename, content])

# Write the data to a CSV file
with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Write the header
    writer.writerow(['name', 'text'])
    # Write the rows
    writer.writerows(data_list)

print(f"Data has been successfully written to {output_file}")