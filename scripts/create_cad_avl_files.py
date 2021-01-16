import csv
import datetime
import os.path
import json
import collections
from os import listdir

OrderedDict = collections.OrderedDict
# aliases
inputdir = os.path.join(os.getcwd(), 'inputfiles', 'cad')

# Input start date from the user
startDateInput = "2020/08/25"
# startDateInput = input("Enter start date in the format yyyy/mm/dd: ")
startDateInputArray = startDateInput.split("/")
startDate = datetime.datetime(int(startDateInputArray[0]), int(startDateInputArray[1]), int(startDateInputArray[2]))

# check if target directory exists, else create one
os.chdir('../mysite/dataengineering/templates')
targetdir = os.getcwd()
if os.path.isdir(targetdir) is False:
    os.mkdir(targetdir)

header = []

# read data from .csv files
for filename in listdir(inputdir):
    # create map of file names and their corresponding json data objects
    dict = {}
    print('Reading data from file ', filename)
    csv_file = open(os.path.join(inputdir, filename), 'r')
    data = csv_file.readlines()
    # update header with 1st row
    header = data[0].split(",")

    # Create the table's row data
    for line in data[1:]:
        row = line.split(",")
        recordDate = datetime.datetime.strptime(row[0], '%Y-%m-%d')
        diff = (recordDate - startDate).days + 1
        if diff in dict.keys():
            data = dict[diff]
        else:
            data = []
        data.append(row)
        dict[diff] = data
    csv_file.close()

print('Data Read Completed from file', filename, '.Splitting into files per day..\n')
for key in dict.keys():
    targetfile = os.path.join(targetdir, 'cad_table_day_' + str(key) + '.html')
    # write data to file in html table format
    with open(targetfile, 'w') as htmlfile:
        table = "<table>\n"
        # Create the table's column headers
        table += "  <tr>\n"
        for column in header:
            table += "    <th>{0}</th>\n".format(column.strip())
        table += "  </tr>\n"

        # Create the table's row data
        for row in dict[key]:
            table += "  <tr>\n"
            for column in row:
                table += "    <td>{0}</td>\n".format(column.strip())
            table += "  </tr>\n"

        table += "</table>"
        htmlfile.writelines(table)
        htmlfile.close()

print("All Files created successfully!")