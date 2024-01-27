import os
from pathlib import Path
from datetime import datetime
from crontab import CronTab

HOME_FOLDER = Path.home()
PACKAGE_FOLDER = HOME_FOLDER / ".local/bin/wiggler"
BASE_FOLDER = HOME_FOLDER / 'WiggleR'
IMG_FOLDER = BASE_FOLDER / "Pictures"

def picture(folder = IMG_FOLDER):
    now = datetime.now()
    fileName = now.strftime("%Y-%m-%d-%H-%M")
    filePath = folder / f"{fileName}.jpg"
    os.system(f"libcamera-jpeg --width 1024 --height 768 --nopreview -t 1 -o {filePath}")

def start_recording(minutes: int = 1):
    cron = CronTab(user=os.getlogin())
    cron.remove_all(comment='wiggler recording')
    job = cron.new(command=f'{PACKAGE_FOLDER} --picture', comment='wiggler recording')
    job.minute.every(minutes)
    cron.write()

def stop_recording():
    cron = CronTab(user=os.getlogin())
    cron.remove_all(comment='wiggler recording')
    cron.write()