# https://www.w3resource.com/python-exercises/csv/python-csv-exercise-2.php

import csv

with open('/home/craig/Desktop/python_challneges/csv_files/read_tab_delim/countries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')

    for line in csv_reader:
        str_line = '\t'.join(line)
        print(str_line)