import csv
import datetime
import os.path
import json
import collections
from os import listdir

# aliases
OrderedDict = collections.OrderedDict
header = ["EVENT_NO_TRIP", "EVENT_NO_STOP",	"OPD_DATE",	"VEHICLE_ID", "METERS",	"ACT_TIME",
          "VELOCITY", "DIRECTION",	"RADIO_QUALITY",	"GPS_LONGITUDE",	"GPS_LATITUDE",
          "GPS_SATELLITES",	"GPS_HDOP",	"SCHEDULE_DEVIATION"]

inputdir = os.path.join(os.getcwd(), 'inputfiles')

# Input start date from the user
startDateInput = input("Enter start date in the format yyyy/mm/dd: ")
startDateInputArray = startDateInput.split("/")
startDate = datetime.datetime(int(startDateInputArray[0]), int(startDateInputArray[1]), int(startDateInputArray[2]))

# check if target directory exists, else create one
os.chdir('../mysite/dataengineering/static/dataengineering')
targetdir = os.getcwd()
if os.path.isdir(targetdir) is False:
    os.mkdir(targetdir)

# read data from .tsv files
for filename in listdir(inputdir):
    # create map of file names and their corresponding json data objects
    dict = {}
    print('Reading data from file ', filename)
    tsv_file = open(os.path.join(inputdir, filename), 'r')
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    # skip the headers
    next(read_tsv, None)
    for row in read_tsv:
        if row[2] is None:
            continue
        recordDate = datetime.datetime.strptime(row[2], '%d-%b-%y')
        diff = (recordDate - startDate).days + 1
        if diff in dict.keys():
            data = dict[diff]
        else:
            data = []
        data.append(OrderedDict(zip(header, row)))
        dict[diff] = data
    tsv_file.close()

    print('Data Read Completed from file', filename, '.Splitting into files per day..\n')
    for key in dict.keys():
        targetfile = os.path.join(targetdir, 'day' + str(key) + '.json')
        # write data to file in json format
        with open(targetfile, 'a') as jsonfile:
            json.dump(dict[key], jsonfile, indent=2)
            jsonfile.close()

print("All Files created successfully!")
