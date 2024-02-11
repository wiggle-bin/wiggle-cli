import os
from pathlib import Path
from datetime import datetime
import csv

HOME_FOLDER = Path.home()
BASE_FOLDER = HOME_FOLDER / 'WiggleR'
DATA_FOLDER = BASE_FOLDER / "Data"
TAG_FILE = DATA_FOLDER / "tags.csv"

def count_lines_in_csv(filePath = TAG_FILE):
    with open(filePath, 'r') as file:
        lines = file.readlines()

    return len(lines)

def create_csv_file(filePath = TAG_FILE):
    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date'])

def add_line_to_csv(line, filePath = TAG_FILE):    
    with open(filePath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(line)

def tag():
    create_csv_file()
    now = datetime.now()
    add_line_to_csv([now])
    print(f"Tag added {now}")