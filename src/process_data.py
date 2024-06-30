import pandas as pd
import csv

def summary_statistic(name_file):
    try:
        # Summary statistics
        df = pd.read_csv(f'data/{name_file}')
        print("\nSummary statistics:")
        print(df.describe())
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

def group_by_column(name_file):
    # Group by a column and calculate the mean
    df = pd.read_csv(f'data/{name_file}')
    try:
        print("\nMean by group:")
        print(df.groupby('category')['value'].mean())
    except Exception as e:
        print("An error occurred during grouping and mean calculation, because the data not provide", e)

def sorting_data(name_file, column_name):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f'data/{name_file}')

        # Sort the DataFrame by a specific column
        sorted_df = df.sort_values(by=column_name)

        # Write the sorted DataFrame back to a CSV file
        sorted_df.to_csv(f'data/sorted_{name_file}', index=False)
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

def rows(name_file):
    try:
        # Open the CSV file
        name_file = f'data/{name_file}'
        with open(name_file, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Initialize a variable to count the rows
            row_count = 0
            
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Increment the row count for each row
                row_count += 1
            
            # Print the total number of rows
            print(f"Total rows:{row_count} (including header of file)")
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

def find_data(name_file, value):
    try:
        # print(name_file)
        # Define the value to search for
        search_value = value

        # Open the CSV file
        name_file = f'data/{name_file}'
        with open(name_file, 'r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Initialize a list to store matching rows
            matching_rows = []
            
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Check if the search value is present in the row
                if search_value in row:
                    # If the value is found, add the entire row to the list of matching rows
                    matching_rows.append(row)
            
            # Print the matching rows
            if matching_rows:
                print("Matching rows:")
                for row in matching_rows:
                    print(row)
            else:
                print("No matching rows found.")
    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        
    except Exception as e:
        print("An error occurred:", e)

def delete_data(name_file, column_name, value_delete):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f'data/{name_file}')

        # Filter the DataFrame to exclude rows with the specified column value
        filtered_df = df[df[column_name] != value_delete]

        # Write the filtered DataFrame back to a new CSV file
        filtered_df.to_csv(f'data/filtered_{name_file}', index=False)

    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")

    except Exception as e:
        print("An error occurred:", e)

def count_data_in_csv(name_file, column_name, data_to_find):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f'data/{name_file}')

        # Count occurrences of the specified data in the specified column
        count = df[df[column_name] == data_to_find].shape[0]

        return count

    except FileNotFoundError:
        print(f"Error: File '{name_file}' not found.")
        return -1

    except Exception as e:
        print("An error occurred:", e)
        return -1

# Example usage:
# file_path = "example.csv"
# column_name = "Column1"
# data_to_find = "desired_data"

# count = count_data_in_csv(file_path, column_name, data_to_find)
# if count != -1:
#     print(f"Number of occurrences of '{data_to_find}' in '{column_name}': {count}")