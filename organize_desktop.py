import os
import shutil
from pathlib import Path

desktop_path = Path.home() / "Desktop"

file_type_directories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css', '.sh', '.bat'],
    'Others': []
}

for folder in file_type_directories.keys():
    target_dir = desktop_path / folder
    if not target_dir.exists():
        target_dir.mkdir()

def move_files():
    for item in desktop_path.iterdir():
        if item.is_file():
            moved = False
            for folder, extensions in file_type_directories.items():
                if item.suffix.lower() in extensions:
                    target_dir = desktop_path / folder
                    shutil.move(str(item), str(target_dir / item.name))
                    moved = True
                    break
            if not moved:
                others_dir = desktop_path / 'Others'
                shutil.move(str(item), str(others_dir / item.name))

if __name__ == "__main__":
    move_files()
    print("Desktop has been organized.")
