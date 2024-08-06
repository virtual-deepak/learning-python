import csv
from os import write

def read_csv(file_name, delimiter):
    with open(file_name, 'r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            print(f'{" | ".join(row)}')
            # Individual cells can be read as row[0], row[1]...

def write_csv(file_name, row, delimiter):
    with open(file_name, 'a', newline='\n') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row)
        
#read_csv('./samples/files_to_read/names.csv', ',')
write_csv('./samples/files_to_read/names.csv',
          ['Jane', 'Doe', '35', 'female'],
          ',')