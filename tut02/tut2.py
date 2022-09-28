from openpyxl.styles.borders import Border
import csv
from openpyxl.styles import borders
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter as gl
import pandas as pd

#Defining the function which takes mod as its default argument.
def octant_transition_count(mod=5000):
    # Here I am using Pandas library to read the excel file "input_octant_transition_identify.xlsx".
    dataframe = pd.read_excel("input_octant_transition_identify.xlsx")
    # In order to work with excel we have to use load_workbook library
    wbook = load_workbook("input_octant_transition_identify.xlsx")
    # Now, we work with active sheet.
    wsheet = wbook.active
    size = len(dataframe['Time'].tolist())
    # list for containing uavg, vavg and wavg values.
    alist = ["U Avg", "V Avg", "W Avg"]
    u_meanlist = dataframe['U'].mean()  # calculating mean of u column.
    v_meanlist = dataframe['V'].mean()  # calculating mean of v column.
    w_menlist = dataframe['W'].mean()  # calculating mean of w column.
    u_1 = dataframe['U'].tolist()  # storing u in ---list
    v_1 = dataframe['V'].tolist()  # storing v in ---list
    w_1 = dataframe['W'].tolist()  # storing w in ---list
octant_transition_count()