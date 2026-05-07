import csv
import os

def check_file_exists(file_name):
    if os.path.exists(file_name):
        print(f"File '{file_name}' exists.")
        return True
    else:
        print(f"File '{file_name}' does not exist.")
        return False

def read_csv(file_name):
    if check_file_exists(file_name):
        with open(file_name, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)

def write_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["ID", "Name", "Age", "City"])
        for row in data:
            csv_writer.writerow(row)

def update_csv(file_name, updated_data):
    if check_file_exists(file_name):
        rows = []
        with open(file_name, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

        for i, row in enumerate(rows):
            if row[0] == updated_data[0]:
                rows[i] = updated_data

        with open(file_name, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

def delete_row(file_name, row_to_delete):
    if check_file_exists(file_name):
        rows = []
        with open(file_name, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)

        rows = [row for row in rows if row[0] != row_to_delete[0]]

        with open(file_name, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

data = [
    [1, 'Alice', 30, 'New York'],
    [2, 'Bob', 25, 'Los Angeles'],
    [3, 'Charlie', 35, 'Chicago']
]

file_path = 'people.csv'

write_csv(file_path, data)

print("\nReading CSV:")
read_csv(file_path)

updated_data = [2, 'Bob', 26, 'San Francisco']
update_csv(file_path, updated_data)

delete_row(file_path, [1, 'Alice', 30, 'New York'])

print("\nUpdated CSV after changes:")
read_csv(file_path)