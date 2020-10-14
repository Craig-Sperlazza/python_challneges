# https://www.w3resource.com/python-exercises/csv/python-csv-exercise-4.php

import csv

with open('/home/craig/Desktop/python_challneges/csv_files/read_dict/departments.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for item in csv_reader:
        print(item)
        print(item['department_name'])
    
    # for key, value in enumerate(csv_reader):
    #     print(f"The key:value is {key}:{value}")
