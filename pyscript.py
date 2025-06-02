import os
import shutil


def organize_by_extension(folder_path):
    if not os.path.exists(folder_path):
        return "Folder does not exist"

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder_path, ext.upper())
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))
    return "Files organized by extension."
