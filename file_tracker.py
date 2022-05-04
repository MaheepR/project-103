import sys
import time
import random

import os
import shutil
#import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/Dell/Downloads/projee-102"
to_dir = "D:/Document_Files"

# Event Hanlder Class

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created !")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")

    def on_modified(self,event):
        print(f"Someone modified {event.src_path}")

    def on_moved(self,event):
        print(f"Someone moved {event.src_path} to {event.reach_path}")

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stop!")
    observer.stop()