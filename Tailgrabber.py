import requests
import re

# Define the file paths
input_file = r'X:\Users\XXX\Desktop\XXX.txt'
output_file = r'X:\Users\XXX\Desktop\XXX.txt'

# Read URLs from the input file
with open(input_file, 'r') as file:
    urls = file.readlines()

# Process each URL and write the extracted coordinates to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    for url in urls:
        # Open the URL and retrieve the response
        response = requests.get(url.strip())
        response_text = response.text

        # Extract the coordinates using regular expressions
        pattern = r'lat=([-]?\d+\.\d+)&amp;lng=([-]?\d+\.\d+)'
        match = re.search(pattern, response_text)

        if match:
            lat = match.group(1)
            lng = match.group(2)
            coordinates = lat + ',' + lng
            file.write('URL: {}\n'.format(url.strip()))
            file.write('Extracted Coordinates: {}\n'.format(coordinates))
            file.write('\n')
        else:
            file.write('URL: {}\n'.format(url.strip()))
            file.write('Extracted Coordinates: Not Found\n\n')

print('Extracted coordinates saved to', output_file)
