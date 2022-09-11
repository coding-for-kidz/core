import os
from pathlib import PurePath


def working_dir():
    return PurePath(os.getcwd())


def file_dir():
    return PurePath(os.path.dirname(os.path.realpath(__file__)))


def cfk_dir() -> PurePath:
    current_dir = PurePath(working_dir())
    parts = current_dir.parts
    if parts[-1] == "coding-for-kidz":
        return current_dir
    mod_dir = PurePath("")
    for item in parts:
        mod_dir /= item
        if item == "coding-for-kidz":
            return mod_dir
    return current_dir
