import os

def list_dir(folder_name):
    for file_name in os.listdir(folder_name):
        print(file_name)

list_dir("./samples/files")