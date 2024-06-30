import pandas as pd
import csv

def read_csv(name_file):
    try:
        print(f"Name file: {name_file}")
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f'data/{name_file}')
        # Display the first few rows of the DataFrame
        print(df.head())
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

def show_column(name_files):
    try:
        # Open the CSV file
        name_file = f'data/{name_files}'
        with open(name_file, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Read the header row to get column names
            header = next(csv_reader)
            
            # Display the column names
            print("Column Names:", header)
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

def get_column(name_files, column_name):
    try:
        # Open the CSV file
        name_file = f'data/{name_files}'
        with open(name_file, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Read the header row to get column names
            header = next(csv_reader)
            
            # Find the index of the column by name
            column_index = header.index(column_name)
            
            # Extract the column data
            column_data = [row[column_index] for row in csv_reader]
            
            # Display the extracted column data with formatting
            print(f"Column '{column_name}' Data:")
            for data in column_data:
                print(data)
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

