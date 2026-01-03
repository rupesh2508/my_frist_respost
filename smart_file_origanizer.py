 import os
import shutil

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            name, ext = os.path.splitext(file)
            ext = ext[1:]

            if ext == "":
                continue

            dest = os.path.join(folder_path, ext)
            if not os.path.exists(dest):
                os.makedirs(dest)

            shutil.move(os.path.join(folder_path, file), dest)

    print("Files organized successfully!")

if _name_ == "_main_":
    path = input("Enter folder path to organize: ")
    organize_files(path)
