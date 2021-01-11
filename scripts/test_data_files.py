import csv
import datetime
import os.path
import json
from os import listdir

# directory of tsv files
inputdir = os.path.join(os.getcwd(), 'inputfiles')

# Input start date from the user
startDateInput = input("Enter start date in the format yyyy/mm/dd: ")
startDateInputArray = startDateInput.split("/")
startDate = datetime.datetime(int(startDateInputArray[0]), int(startDateInputArray[1]), int(startDateInputArray[2]))

# check if target directory exists, else create one
os.chdir('../mysite/dataengineering/static/dataengineering')
targetdir = os.getcwd()
if os.path.isdir(targetdir) is False:
    print("target directory does not exist.")
    exit(1)

last_day = 0
# create map of file names and the number of records
dict = {}
# read data from .tsv files
for filename in listdir(inputdir):
    print('Reading data from file', filename)
    tsv_file = open(os.path.join(inputdir, filename), 'r')
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    # skip the headers
    next(read_tsv, None)
    for row in read_tsv:
        if row[2] is None:
            continue
        recordDate = datetime.datetime.strptime(row[2], '%d-%b-%y')
        diff = (recordDate - startDate).days + 1
        last_day = max(last_day, diff)
        count = dict.get(diff, 0)
        dict[diff] = count+1
    tsv_file.close()

print('Data Read Completed from tsv files. Comparing now with json files..')
for key in range(1, last_day+1):
    targetfile = os.path.join(targetdir, 'day' + str(key) + '.json')
    # read data from file in json format
    with open(targetfile, 'r') as jsonfile:
        j = json.load(jsonfile)
        records_in_json_file = len(j)
        records_in_tsv = dict.get(key, 0)
        if records_in_json_file != records_in_tsv:
            print("day {0} missing {1} records".format(key, abs(records_in_json_file - records_in_tsv)))

print("All Files checked successfully!")
