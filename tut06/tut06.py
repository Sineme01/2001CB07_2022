import xlsxwriter as xl
import pandas as pd
from openpyxl.styles.borders import Border
from openpyxl.styles import borders
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter as gl
import datetime as dt
from platform import python_version
import math as ma
import os
from datetime import datetime
start_time = datetime.now()
# importing os module
def R(): return map(int, input().split())


# This is a python program to demonstrate the use of os.mkdir() method.
path = 'output'
try:
    os.mkdir(path)  # create a folder in my directory named output.
except OSError as error:
    print(error)


def Check_Days(s):
    ps = s
    j, t = ps.split(" ")
    date, month, year = j.split("-")
    map_months = {'01': "January", '02': "February", "03": "March", "04": "April", "05": "May", "06": "June", '07': 'July', "08": "August", '09': "September", "10": 'October',
                  '11': "November", "12": "December"}

   # strptime() is another method available in DateTime which is used to format the time stamp.
    x = dt.datetime.strptime(
        f'{map_months[month]} {date}, {year}', '%B %d, %Y').strftime('%A')

    return x


def func_sort_date(date):
    dateList = list(date)
    siz = len(dateList)
    for i in range(siz):
        var = dateList[i].split("-")
        flag = var[2]+var[1]+var[0]
        dateList[i] = flag
    # sorting the date list for proper view of attendance report.
    dateList.sort()
    for i in range(siz):
        var = dateList[i][-2:]+'-'+dateList[i][-4:-2]+'-'+dateList[i][:4]
        dateList[i] = var

    return dateList
