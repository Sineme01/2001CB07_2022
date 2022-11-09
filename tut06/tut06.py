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