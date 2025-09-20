from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from pathlib import Path

class MyHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if not event.is_directory:
            file_path = Path(event.dest_path)
            print(f"{file_path.name} baru dibuat!")

observer = Observer()
observer.schedule(MyHandler(), path="C:/Users/tsugaide/Downloads", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
