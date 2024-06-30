#this main function of this project

import argparse
import random
import string
import src.read_data as read
import src.create_data as create
import src.process_data as process

data=""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Final Project Python')
    parser.add_argument('--url', help='URL of the data to download, example: python3 main.py --url www.test.com')
    parser.add_argument('--read_data', help='read file .csv which must save and place on data/ directory example (test is name file, you must make sure your data on csv format and dont write file extension on the command): python3 main.py --read_data test')
    parser.add_argument('--column', help='using for get data based on column, example: python3 main.py --read_data test --column id')
    parser.add_argument('--show_column', help='using for know name of all column, example: python3 main.py --show_column test')
    parser.add_argument('--statistic', help='using for statistic of csv, example: python3 main.py --statistic test')
    parser.add_argument('--group_column', help='using for group by column of csv, example: python3 main.py --group_column test')
    parser.add_argument('--sort_data', help='using for sort by column of csv and you must using column command to sort the data, example: python3 main.py --sort_data test --column userId')
    parser.add_argument('--delete_data', help='using for delete by column of csv and used together with column command, must be used together with value_data and column arguments, example: python3 main.py --delete_data test --value_data 1 --column id')
    parser.add_argument('--value_data', help='using set Value, must using together with delete_data, find_data, and find_count, example: python3 main.py --find_data test --value_data 1')
    parser.add_argument('--count_rows', help='using to count rows in file .csv, example: python3 main.py --count_rows test')
    parser.add_argument('--find_data', help='using to find data on .csv file, example: example: python3 main.py --find_data test --value_data 1')
    parser.add_argument('--find_count', help='using to find data on specific column and to know how much it is, example: python3 main.py --find_count customers-100 --column First Name --value_data Sheryl')
    args = parser.parse_args()

    if args.url:
        # https://jsonplaceholder.typicode.com/posts #for the website of JSON data example
        data = create.download_data(args.url)
        random_alphabet = random.choice(string.ascii_letters) #make a random alphabet to save the file
        if data:
            csv_filename = f"data/{random_alphabet}.csv"
            create.convert_to_csv(data, csv_filename)
            print("Data has been converted to CSV:", csv_filename)
    elif args.read_data:
        data = f"{args.read_data}.csv"
        column = args.column
        if args.column:
            read.get_column(data, column)
        else:
            read.read_csv(data)
            # print(f"file {data}")   
    elif args.show_column:
        data = f"{args.show_column}.csv"
        read.show_column(data)
    elif args.statistic:
        data = f"{args.statistic}.csv"
        process.summary_statistic(data)
    elif args.group_column:
        data = f"{args.group_column}.csv"
        process.group_by_column(data)
    elif args.sort_data:
        if args.column:
            data = f"{args.sort_data}.csv"
            process.sorting_data(data, args.column)
    elif args.delete_data:
        if args.value_data:
            if args.column:
                data = f"{args.delete_data}.csv"
                process.delete_data(data, args.column, args.value_data)
    elif args.count_rows:
        data = f"{args.count_rows}.csv"
        process.rows(data)
    elif args.find_data:
        data = f"{args.find_data}.csv"
        if args.value_data:
            process.find_data(data, args.value_data)
    elif args.find_count:
        data = f"{args.find_count}.csv"
        if args.column:
            if args.value_data:
                count = process.count_data_in_csv(data, args.column, args.value_data)
                if count != -1:
                    print(f"Number of occurrences of '{args.value_data}' in '{args.column}': {count}")
                else:
                    print("Error")
    else:
        print("Please provide correct command")
