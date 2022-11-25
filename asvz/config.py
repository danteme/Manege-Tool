"""Reads config file and prepares input file list.

Tool to configure input and output directories and
create list of input files.

Functions
---------
    read(argnum) -> list
    get_files(directory, form) -> list
"""

#only needed when Python ver < 3.9
from __future__ import annotations
#end of: only needed when Python ver < 3.9

import glob
import sys


def read(argnum: int) -> list[str]:
    """Read config file and return a list of config values."""
    try:
        config_values = []
        with open("config", "r", encoding="utf-8") as config_file:
            for row in config_file.readlines():
                if row[0:1] != "#" and row[0:2] != "\n":
                    config_values.append(row[:-1])
    except IOError:
        print("  ERROR: configuration file not readable")
        sys.exit()

    if len(config_values) == argnum:
        return config_values

    print("  ERROR: configuration file has wrong format")
    sys.exit()


def get_files(directory, form):
    """Read all poll files in directory and return a list of all files."""
    files = []
    for element in glob.glob(directory+form):
        files.append(element)
    return files
