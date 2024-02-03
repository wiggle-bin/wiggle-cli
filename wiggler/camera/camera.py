import os
from pathlib import Path
from datetime import datetime
from picamera2 import Picamera2
import time
from PIL import Image

HOME_FOLDER = Path.home()
PACKAGE_FOLDER = HOME_FOLDER / ".local/bin/wiggler"
BASE_FOLDER = HOME_FOLDER / 'WiggleR'
IMG_FOLDER = BASE_FOLDER / "Pictures"

def picture(folder = IMG_FOLDER):
    now = datetime.now()
    fileName = now.strftime("%Y-%m-%d-%H-%M-%S")
    filePath = folder / f"{fileName}.jpg"
    picture_gray(filePath)

def picture_color(filePath):
    picam2 = Picamera2()
    picam2.start()
    time.sleep(2)
    picam2.capture_file(str(filePath))
    picam2.close()

def picture_gray(filePath):
    grey = picture_yuv()
    image = Image.fromarray(grey)
    image.save(filePath)
    print(f"Saved grayscale picture to {filePath}")

def picture_yuv():
    WIDTH = 1024
    HEIGHT = 768
    picam2 = Picamera2()
    config = picam2.create_preview_configuration({'format': 'YUV420', 'size': (WIDTH, HEIGHT)})
    picam2.configure(config)
    picam2.start()
    time.sleep(2)
    yuv = picam2.capture_array()
    grey = yuv[:HEIGHT, :WIDTH]
    picam2.close()
    return grey

def pictures():
    seconds = 5
    try:
        while True:
            picture()
            time.sleep(seconds)
    except KeyboardInterrupt:
        print("Stopped by User")

def start_recording():
    os.system("systemctl --user start wiggle_record.service")

def stop_recording():
    os.system("systemctl --user stop wiggle_record.service")
