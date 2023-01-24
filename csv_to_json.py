import csv
import json

csv_file_path = "....../csv_to_json.csv"    # Full path to CSV file

# To a DICT
file = open(csv_file_path, "r", encoding = "utf-8")
dictonary = list(csv.DictReader(file, delimiter=";"))
file.close()

for entry in dictonary:
    #print(entry)
    print(entry['columA'])
