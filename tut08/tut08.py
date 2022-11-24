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

    ls = []
    lp = []

    for i in com1[::2]:
        a = i.split(",")
        b = a[0]
        b = b.split('to')
        Array2bat = b[1][1:]
        ball, Array1Bowl = b[0].split(" ", 1)
        Array1Bowl = Array1Bowl[:-1]
        p = b[0].split(" ", 2)
        u = 1
        if (Array2bat not in dict_Array2Players):
            lp.append(Array2bat)
        if (Array1Bowl not in dict_Array1Players):
            ls.append(Array1Bowl)
    for i in com2[::2]:
        a = i.split(",")
        b = a[0]
        b = b.split('to')
        Array1bat = b[1][1:]
        ball, Array2Bowl = b[0].split(" ", 1)
        Array2Bowl = Array2Bowl[:-1]
        if (Array1bat not in dict_Array1Players):
            ls.append(Array1bat)
        if (Array2Bowl not in dict_Array2Players):
            lp.append(Array2Bowl)
    ls = set(ls)
    lp = set(lp)
    makei = []
    makep = []
    deli = []
    delp = []

    for j in ls:
        for i in dict_Array1Players:
            if (j.lower() in dict_Array1Players[i].lower()):
                makei.append([j, dict_Array1Players[i]])
                deli.append(dict_Array1Players[i])
    for j in lp:
        for i in dict_Array2Players:
            if (j.lower() in dict_Array2Players[i].lower()):
                makep.append([j, dict_Array2Players[i]])
                delp.append(dict_Array2Players[i])

    for j in deli:
        del dict_Array1Players[j]
    for j in delp:
        del dict_Array2Players[j]
    for i, j in makei:
        dict_Array1Players[i] = j
    for i, j in makep:
        dict_Array2Players[i] = j
    BatterArray2 = []
    BatterArray21 = []
    BowlerArray1 = []
    BowlerArray11 = []
    BatterArray1 = []
    BatterArray11 = []
    BowlerArray2 = []
    BowlerArray21 = []
    OutArray2 = {}
    for i in dict_Array2Players:
        OutArray2[i] = "not out"
    OutArray1 = {}
    for i in dict_Array1Players:
        OutArray1[i] = "not out"
    BatterArray2Run = {}
    for i in dict_Array2Players:
        BatterArray2Run[i] = 0
    BatterArray1Run = {}
    for i in dict_Array1Players:
        BatterArray1Run[i] = 0
    BatterArray2Ball = {}
    for i in dict_Array2Players:
        BatterArray2Ball[i] = 0
    BatterArray1Ball = {}
    for i in dict_Array1Players:
        BatterArray1Ball[i] = 0
    BatterArray24s = {}
    for i in dict_Array2Players:
        BatterArray24s[i] = 0
    BatterArray14s = {}
    for i in dict_Array1Players:
        BatterArray14s[i] = 0
    BatterArray26s = {}
    for i in dict_Array2Players:
        BatterArray26s[i] = 0
    BatterArray16s = {}
    for i in dict_Array1Players:
        BatterArray16s[i] = 0

    Array2b = 0
    Array2lb = 0
    Array2w = 0
    Array2nb = 0
    Array2p = 0
    Array1b = 0
    Array1lb = 0
    Array1w = 0
    Array1nb = 0
    Array1p = 0
    Array2powerRun = 0
    Array1powerRun = 0
    Array1BowlerOver = {}
    for i in dict_Array1Players:
        Array1BowlerOver[i] = 0
    Array2BowlerOver = {}
    for i in dict_Array2Players:
        Array2BowlerOver[i] = 0
    Array1BowlerMaiden = {}
    for i in dict_Array1Players:
        Array1BowlerMaiden[i] = 0
    Array2BowlerMaiden = {}
    for i in dict_Array2Players:
        Array2BowlerMaiden[i] = 0
    Array2BowlerRun = {}
    for i in dict_Array2Players:
        Array2BowlerRun[i] = 0
    Array1BowlerRun = {}
    for i in dict_Array1Players:
        Array1BowlerRun[i] = 0
    Array2BowlerWicket = {}
    for i in dict_Array2Players:
        Array2BowlerWicket[i] = 0
    Array1BowlerWicket = {}
    for i in dict_Array1Players:
        Array1BowlerWicket[i] = 0
    Array2BowlerNb = {}
    for i in dict_Array2Players:
        Array2BowlerNb[i] = 0
    Array1BowlerNb = {}
    for i in dict_Array1Players:
        Array1BowlerNb[i] = 0
    Array2BowlerWd = {}
    for i in dict_Array2Players:
        Array2BowlerWd[i] = 0
    Array1BowlerWd = {}
    for i in dict_Array1Players:
        Array1BowlerWd[i] = 0
    fallArray1 = []
    fallArray2 = []
    totalrun1 = 0
    totalrun2 = 0
    wicket1 = 0
    wicket2 = 0
    d_run = {'1': 1, '2': 2, '3': 3, 'four': 4, 'six': 6, 'five': 5}

    prev = '0'
    pt = 0
    u = 0
    flag = 0


ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()

end_time = datetime.datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
