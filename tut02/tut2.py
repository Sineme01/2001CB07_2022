from openpyxl.styles.borders import Border
import csv
from openpyxl.styles import borders
from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter as gl
import pandas as pd

# Defining the function which takes mod as its default argument.


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
    for i in range(3):
        wsheet[gl(i+5)+"1"] = alist[i]
    meanval = [u_meanlist, v_meanlist, w_menlist]
    for i in range(3):
        wsheet[gl(i+5)+"2"] = meanval[i]
    blist = ["U'=U-Uavg", "V'=V-Vavg", "W'=W-Wavg"]
    clist = [u_1, v_1, w_1]
    for i in range(3):
        wsheet[gl(i+8)+"1"] = blist[i]
    for i in range(3):
        for j in range(1, size+1):
            wsheet[gl(i+8)+str(j+1)] = clist[i][j-1]-meanval[i]
    dictionary = {'+++': "+1", "++-": "-1", "-++": "+2", "-+-": "-2",
                  "--+": "+3", "---": "-3", "+-+": "+4", "+--": "-4"}
    wsheet[gl(11)+"1"] = "Octat"
    # The loop below is used to compute octant values.
    for i in range(1, size+1):
        x = ""
        for j in range(8, 11):
            if (wsheet[gl(j)+str(i+1)].value >= 0):
                x += '+'
            else:
                x += '-'
        wsheet[gl(11)+str(i+1)] = dictionary[x]
    listf = ["+1", "-1", "+2", "-2", "+3", "-3", "+4", "-4"]
    for i in range(len(listf)):
        wsheet[gl(i+14)+"1"] = listf[i]
    wsheet[gl(13)+"2"] = "Overall Count"
    wbook.save("output_octant_transition_identify.xlsx")


octant_transition_count()
