import json
import csv
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class FileParser(ABC):
    @abstractmethod
    def parse_file(self, file_path):
        pass


class CSVParser(FileParser):
    def parse_file(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]


class JSONParser(FileParser):
    def parse_file(self, file_path):
        with open(file_path) as jsonfile:
            return json.load(jsonfile)


class XMLParser(FileParser):
    def parse_file(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        result = []
        for child in root:
            result.append(child.attrib)
        return result


class FileReader:
    def __init__(self, file_parser):
        self.file_parser = file_parser

    def read_file(self, file_path):
        return self.file_parser.parse_file(file_path)


file_reader = FileReader(CSVParser())
data = file_reader.read_file("/Users/pradyumna.galnimkar/Downloads/PQ-4057.csv")
print(data)