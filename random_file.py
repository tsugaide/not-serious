import os
import random

downloads_folder = os.path.expanduser("~/Downloads")

file_types = [".txt", ".jpg", ".png", ".pdf", ".docx", ".mp3", ".zip", ".rar", ".exe", ".mp4"]

jumlah_file = 15

for i in range(jumlah_file):
    ext = random.choice(file_types)
    
    file_name = f"dummy_file_{i+1}{ext}"
    
    file_path = os.path.join(downloads_folder, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Ini adalah file dummy ke-{i+1} dengan ekstensi {ext}\n")
    
    print(f"✅ Dibuat: {file_path}")

print("Selesai! 🎉")
