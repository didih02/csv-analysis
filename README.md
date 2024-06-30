# This project is used for analysis CSV data. There are some function which can be use:

--url, help=URL of the data to download, example: python3 main.py --url www.test.com

--read_data, help=read file .csv which must save and place on data/ directory example test is name file, you must make sure your data on csv format and dont write file extension on the command: python3 main.py --read_data test

--column, help=using for get data based on column, example: python3 main.py --read_data test --column id

--show_column, help=using for know name of all column, example: python3 main.py --show_column test

--statistic, help=using for statistic of csv, example: python3 main.py --statistic test

--group_column, help=using for group by column of csv, example: python3 main.py --group_column test

--sort_data, help=using for sort by column of csv and you must using column command to sort the data, example: python3 main.py --sort_data test --column userId

--delete_data, help=using for delete by column of csv and used together with column command, must be used together with value_data and column arguments, example: python3 main.py --delete_data test --value_data 1 --column id

--value_data, help=using set Value, must using together with delete_data, find_data, and find_count, example: python3 main.py --find_data test --value_data 1

--count_rows, help=using to count rows in file .csv, example: python3 main.py --count_rows test

--find_data, help=using to find data on .csv file, example: example: python3 main.py --find_data test --value_data 1

--find_count, help=using to find data on specific column and to know how much it is, example: python3 main.py --find_count customers-100 --column First Name --value_data Sheryl

# On this project, using library, please make sure have this library on your python

argparse =>for arguments on command

random =>random value

string =>string operation

requests =>to get data from website

csv =>CSV reader

pandas =>help to process CSV process
