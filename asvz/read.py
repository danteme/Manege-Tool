#
#   Manege-Tool
#   Version 4.2.0 / 30.07.2022
#   Author Daniel Meier 2022+2021 & T.Wisotzki 2019
#

from csv import reader as csvreader
from datetime import datetime


class ManegeDay:
    def __init__(self, name):
        self.name = name
        self.trainings = list()


class Training:
    def __init__(self, date):
        self.date = date
        self.GETU = list()
        self.TRA = list()
        self.AKRO = list()
        self.SLACK = list()
        self.JONG = list()
        self.VERT = list()
        self.PARC = list()
        self.BREAK = list()
        self.CAN = list()


def poll(poll_to_read):
    # ManegeDay class object with name=Trainingname and trainings=list of dates
    training_day = ManegeDay(poll_to_read)
    with open(poll_to_read, 'r', encoding='utf-8') as csvpoll_to_read:
        csvcontent = csvreader(csvpoll_to_read)
        rownum = 1
        for row in csvcontent:
            if rownum == 1:
                # get all training dates from row list,
                # first and last list objects are '', therefore ignored
                for day in range(1, (len(row)-1)):
                    daydate = datetime.strptime(row[day], "%Y-%m-%d")\
                                                .strftime('%d.%m.%Y')
                    # append a Training class object with training date
                    # to training_day.trainings list
                    training_day.trainings.append(Training(daydate))
            # read TL names and their preferences
            elif rownum >= 3:
                # read discipline from first list object and remove ":"
                tl_discipline = row[0].split(" ")[0].replace(':', '')
                # read TL name from first list object
                tl_name = row[0][(len(row[0].split(" ")[0])+1):]
                # creates list with disciplines of the TL
                tl_discipline = tl_discipline.split("/")
                if len(tl_discipline) > 1:
                    # adds "*" to tl_name if more than one disciplines
                    tl_name = tl_name + "*"
                # iterates through all trainings in Trainingday.trainings
                for i in range(len(training_day.trainings)):
                    # read the wish of TL for specific date
                    wish = row[i+1]
                    if wish.lower() != "Nein".lower():
                        # != "Nein" -> TL can do a training
                        for attr, value in training_day.trainings[i]\
                                                       .__dict__.items():
                            tl_ersatz = ''  # var for saved ersatz record
                            for dis in tl_discipline:
                                # add TL if "Ja" and discipline correct
                                if attr.lower() == dis.lower() and (
                                                   wish.lower() ==
                                                   "Ja".lower()):
                                    value.append(tl_name + ",\n")
                                # if wish == "Unter Vorbehalt"
                                # add TL to Ersatz (attr==CAN)
                                elif attr == 'CAN' and wish.lower() == (
                                             "Unter Vorbehalt".lower()):
                                    disz = ""
                                    for newdisz in tl_discipline:
                                        disz = disz + newdisz
                                    # check that ersatz is only safed once
                                    if tl_ersatz != (disz + " " + tl_name
                                                     + ",\n"):
                                        tl_ersatz = (disz + " " + tl_name
                                                     + ",\n")
                                        value.append(tl_ersatz)
            rownum += 1
    return training_day
