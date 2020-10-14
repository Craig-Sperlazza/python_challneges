import csv

with open('/home/craig/Desktop/python_challneges/csv_files/read_list/employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
     
    csv_list = []

    for line in csv_reader:
        csv_list.append(line)

print(csv_list)
