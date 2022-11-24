from platform import python_version
import sys
import datetime
start_time = datetime.datetime.now()


def scorecard():

    sys.stdout = open('Scorecard.txt', 'wt')
    f = open('team.txt', "r")
    a = f.readlines()
    f1 = open("pak_inns1.txt", "r")
    com1 = f1.readlines()
    f2 = open("india_inns2.txt", "r")
    com2 = f2.readlines()
    Array2 = a[0].split(':')[1]
    Array1 = a[2].split(':')[1]

    Array2_Name = a[0].split('(')[0][:-1]
    Array1_Name = a[2].split('(')[0][:-1]

    Array3 = Array2.split()
    Array2 = Array2.split(',')
    for i in range(len(Array2)):
        if (Array2[i].endswith('\n')):
            Array2[i] = Array2[i][:-1]

    Array1 = Array1.split(',')
    for i in range(len(Array1)):
        if (Array1[i].endswith('\n')):
            Array1[i] = Array1[i][:-1]
    dict_Array1Players = {}
    dict_Array2Players = {}
    for i in Array1:
        dict_Array1Players[i[1:]] = i[1:]
    for i in Array2:
        dict_Array2Players[i[1:]] = i[1:]
    if com1[0].split()[1] in Array3:
        temp = Array1_Name
        Array1_Name = Array2_Name
        Array2_Name = temp
        temp = dict_Array1Players
        dict_Array1Players = dict_Array2Players
        dict_Array2Players = temp
        temp = Array1
        Array1 = Array2
        Array2 = temp


ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()

end_time = datetime.datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
