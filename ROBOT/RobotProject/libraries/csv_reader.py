import os
import csv


class CSVReader:

    @staticmethod
    def read_csv(file_name):
        data = []

        base_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = str(os.path.join(base_dir, 'data', file_name))

        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                data.append(row)

        return data