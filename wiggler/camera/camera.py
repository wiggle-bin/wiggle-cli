import os
from pathlib import Path
from datetime import datetime
from crontab import CronTab

BASE_FOLDER = Path.home() / 'WiggleR'
IMG_FOLDER = f"{BASE_FOLDER}/Pictures"

def picture():
    now = datetime.now()
    fileName = now.strftime("%Y-%m-%d-%H-%M")
    filePath = f"{IMG_FOLDER}/{fileName}.jpg"
    os.system(f"libcamera-jpeg --width 1024 --height 768 --nopreview -t 1 -o {filePath}")
    
def start_recording(minutes: int = 1):
    cron = CronTab(user=os.getlogin())
    cron.remove_all(comment='wiggler recording')
    job = cron.new(command='wiggler camera --picture', comment='wiggler recording')
    job.minute.every(minutes)
    cron.write()

def stop_recording():
    cron = CronTab(user=os.getlogin())
    cron.remove_all(comment='wiggler recording')
    cron.write()