import csv
from pprint import pprint
from src.Fileutilities.Absolutepath import absolute_path


def class_factory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        with open(absolute_path(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
                print(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(class_factory(class_name, row))
        return objects
