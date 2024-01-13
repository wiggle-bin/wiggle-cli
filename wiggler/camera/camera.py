import os
from pathlib import Path
from datetime import datetime
import shutil
from crontab import CronTab

HOME_FOLDER = Path.home()
PACKAGE_FOLDER = HOME_FOLDER / ".local/bin/wiggler"
BASE_FOLDER = HOME_FOLDER / 'WiggleR'
IMG_FOLDER = BASE_FOLDER / "Pictures"
RECORDING_FOLDER = BASE_FOLDER / "Recording"
ACTIVE_RECORDING_FOLDER = RECORDING_FOLDER / "InProgress"

def move_all_files(src_folder, dest_folder):
    for filename in os.listdir(src_folder):
        src_path = os.path.join(src_folder, filename)

        if os.path.isfile(src_path):
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename} to {dest_folder}")

def picture(folder = IMG_FOLDER):
    now = datetime.now()
    fileName = now.strftime("%Y-%m-%d-%H-%M")
    filePath = folder / f"{fileName}.jpg"
    os.system(f"libcamera-jpeg --width 1024 --height 768 --nopreview -t 1 -o {filePath}")

def picture_recording():
    picture(folder = ACTIVE_RECORDING_FOLDER)

def start_recording(minutes: int = 1):
    cron = CronTab(user=os.getlogin())
    cron.remove_all(comment='wiggler recording')
    job = cron.new(command=f'{PACKAGE_FOLDER} --recording picture', comment='wiggler recording')
    job.minute.every(minutes)
    cron.write()

def make_recording_result_folder(files):
    start, _ = os.path.splitext(files[0])
    end, _ = os.path.splitext(files[-1])
    folder = RECORDING_FOLDER / f"{start}--{end}"
    os.makedirs(folder, exist_ok=True)
    return folder

def stop_recording():
    # move recording to destination folder
    files = os.listdir(ACTIVE_RECORDING_FOLDER)
    if (files):
        move_all_files(ACTIVE_RECORDING_FOLDER, make_recording_result_folder(files))
    
    # remove from cron
    cron = CronTab(user=os.getlogin())
    cron.remove_all(comment='wiggler recording')
    cron.write()