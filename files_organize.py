from genericpath import isfile
import os
import shutil

desktop_path = os.path.expanduser("~/Desktop")

file_extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".docx", ".doc", ".pdf", ".txt"],
    "Archives": [".zip", ".rar"]
}

for folder_name in file_extensions:
    if not os.path.exists(os.path.join(desktop_path, folder_name)):
        os.makedirs(os.path.join(desktop_path, folder_name))

for item in os.listdir(desktop_path):
    source_file_path = os.path.join(desktop_path, item)
    if os.path.isfile(source_file_path):
        filename, file_ext = os.path.splitext(item)
        for key, values in file_extensions.items():
            if file_ext in values:
                destination_file_path = os.path.join(desktop_path, key, item)
                shutil.move(source_file_path, destination_file_path)
                print(f"{source_file_path} -> {destination_file_path}")