from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

categories = {
    "image": [".jpg", ".png", ".jpeg"],
    "music": [".mp3"],
    "video": [".mp4"],
    "archieve": [".zip", ".rar", ".7z"],
    "application": [".exe"],
    "document": [".pdf", ".txt", ".docx"]
}

def kategorikan_file(path_file):
    found = False
    for key, exts in categories.items():
        if path_file.suffix.lower() in exts:
            path_file.rename(downloads / key / path_file.name)
            found = True
            break
    
    if not found:
        (downloads / "others").mkdir(exist_ok=True)
        path_file.rename(downloads / "others" / path_file.name)



downloads = Path("~/Downloads").expanduser()

for i in categories:
    (downloads / i).mkdir(exist_ok=True)


for files in downloads.iterdir():
    if files.is_file():
        kategorikan_file(files)
        

print("selesai")
print("Mulai Memonitor.....")

class MyHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if not event.is_directory:
            time.sleep(0.5)
            kategorikan_file(Path(event.dest_path))

observer = Observer()
observer.schedule(MyHandler(), path=str(downloads), recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

