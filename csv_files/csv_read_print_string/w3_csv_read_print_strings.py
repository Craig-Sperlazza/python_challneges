# https://www.w3resource.com/python-exercises/csv/index.php

#takes a csv file and prints out each line as a string

import csv

with open('/home/craig/Desktop/python_challneges/csv_files/csv_read_print_string/departments.csv', 'r') as csv_file:
    csv_read = csv.reader(csv_file)
    for line in csv_read:
        str_line = ", ".join(line)
        print(str_line)



