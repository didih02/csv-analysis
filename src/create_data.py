import requests
import csv

def download_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Assuming the data is in JSON format
        else:
            print("Failed to download data:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)

def convert_to_csv(data, csv_filename):
    if data:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Assuming data is a list of dictionaries where keys are column headers
            writer.writerow(data[0].keys())  # Write header row
            for row in data:
                writer.writerow(row.values())