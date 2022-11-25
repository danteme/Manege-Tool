"""Manege-Tool to assign ASVZ teachers to trainings.

Tool to help assigning the different ASVZ teachers to the specific
trainigs slots based on the teachers preferences and disciplines.

Features
--------
- separate the teachers according to their disciplines
- assign them to the training slots according to their preferences
  into 'want' and 'can' teach
- automaticly prepares basic Word document with training slots, disciplines
  and the teachers preferences
- easy configurations of input and output directories
- automaticly reads and processes files according to configuration

Usage
-----
1. export polls from https://nuudel.digitalcourage.de/ to CSV
   make sure the poll/document language is set to "Deutsch"
2. store the CSV file(s) in the directory specified in the config file
   (default is "./polls/")
3. run the tool $ python main.py
4. the program writes the output documents into the output directory
   specified in the config file (default is ""./assignments/")
"""

__version__ = "4.2.0"
# Version 4.2.0 / 30.07.2022
# Author D. Meier 2022 + 2021
# Derived from Manege-Tool by T.Wisotzki 2019
# Original Source https://github.com/binaarinen/Manege-Tool


import os
import sys

from asvz import config
from asvz import read
from asvz import filewriter


print("processing... input files")

# read configurations and prepare processing
configuration = config.read(2)
in_dir = configuration[0]
out_dir = configuration[1]
if os.path.isdir(in_dir):
    polls = config.get_files(in_dir, "*.csv")  # read all csv files
else:
    print(
        "  ERROR: input directory: "
        + in_dir
        + " not found. Please check the 'config' file"
    )
    sys.exit()

# loop through files and process data
for poll_num, poll in enumerate(polls, start=1):
    Trainingsday = read.poll(poll)
    print(
        " "
        + str(poll_num)
        + "/"
        + str(len(polls))
        + " "
        + str(poll)
        + ".......processing"
    )
    filewriter.Out(Trainingsday, out_dir)
    print(" " + str(poll_num) + "/" + str(len(polls)) + " " + str(poll) + ".......done")

print("completed")
