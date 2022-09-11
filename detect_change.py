import os
import pathlib


def recurse_through_files(root_dir):
    all_files = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            all_files.append(os.path.join(subdir, file))
    return all_files


def get_mod_date(file):
    path = pathlib.Path(file)
    return path.stat().st_mtime


def anything_changed(root_dir):
    recurse_through_files(root_dir)
