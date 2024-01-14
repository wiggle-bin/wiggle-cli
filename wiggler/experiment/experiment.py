import os
from pathlib import Path
from datetime import datetime
import csv

HOME_FOLDER = Path.home()
BASE_FOLDER = HOME_FOLDER / 'WiggleR'
DATA_FOLDER = BASE_FOLDER / "Data"
EXPERIMENTS_FILE = DATA_FOLDER / "experiments.csv"

def count_lines_in_csv(filePath = EXPERIMENTS_FILE):
    with open(filePath, 'r') as file:
        lines = file.readlines()

    return len(lines)

def create_csv_file(filePath = EXPERIMENTS_FILE):
    if not os.path.exists(filePath):
        with open(filePath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'start', 'stop'])

def get_last_entry(filePath = EXPERIMENTS_FILE):
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        last_line = list(reader)[-1]

    return last_line

def add_line_to_csv(line, filePath = EXPERIMENTS_FILE):    
    with open(filePath, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(line)

def log_experiment(tag):
    create_csv_file()
    now = datetime.now()
    add_line_to_csv([now, tag])
    print(f"Experiment logged {now} {tag}")