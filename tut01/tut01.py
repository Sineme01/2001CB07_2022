#importing pandas library for the data frame
import pandas as pd
def octact_identification(mod=5000):
    df = pd.read_csv("octant_input.csv")
    # take average of u,v,w
    uavg = df['U'].mean()
    vavg = df['V'].mean()
    wavg = df['W'].mean()
    o1=[uavg]
    o2=[vavg]
    o3=[wavg]
    for i in range(len(df['Time'])-1):
        o1.append(None)
        o2.append(None)
        o3.append(None)

    
    # make our new output dataframe
    makedata = {"Time": df['Time'], "U": df["U"], "V": df["V"],
                "W": df["W"], "U Avg":o1,"V Avg": o2, "W Avg": o3}
    
  
    
    # make list of u-uavg,v-vavg,w-wavg
    u1 = [i-uavg for i in df['U']]
    v1 = [i-vavg for i in df['V']]
    w1 = [i-wavg for i in df['W']]
    fg = pd.DataFrame(makedata)
    # make new columns of three variables
    fg["U'=U-Uavg"] = u1
    fg["V'=V-Vavg"] = v1
    fg["W'=W-Wavg"] = w1

    OctantValue = []
    a = fg["U'=U-Uavg"].to_list()
    b = fg["V'=V-Vavg"].to_list()
    c = fg["W'=W-Wavg"].to_list()
    OctantValue = []
    d = {'+++': "+1", "++-": "-1", "-++": "+2", "-+-": "-2",
        "--+": "+3", "---": "-3", "+-+": "+4", "+--": "-4"}
    # loop for count total octant
    for i in range(len(a)):
        x = ""
        if (a[i] < 0):
            x += '-'
        else:
            x += '+'
        if (b[i] < 0):
            x += '-'
        else:
            x += '+'
        if (c[i] < 0):
            x += '-'
        else:
            x += '+'
        OctantValue.append(d[x])
    fg["Octant"] = OctantValue

    data = {"": [None], "OctantID": "Overall Cost", 1: [OctantValue.count('+1')], -1: [OctantValue.count('-1')], 2: [OctantValue.count('+2')], -2: [OctantValue.count('-2')],
            3: [OctantValue.count('+3')], -3: [OctantValue.count('-3')], 4: [OctantValue.count('+4')], -4: [OctantValue.count('-4')]}
    #make another dataframe for our final answer
    h = pd.DataFrame(data)
    t = mod
    new_row = {'': "User Input", "OctantID": "Mod"+" "+str(t)}
    h = h.append(new_row, ignore_index=True)
    length=len(df['Time'])

    for i in range(0, length, t):
        if (i+t-1 >= length):
            x = str(i)+"-"+str(29745)
        else:
            x = str(i)+"-"+str(i+t-1)

        j = {"OctantID": x, 1: OctantValue[i:i+t].count('+1'), -1: OctantValue[i:i+t].count('-1'), 2: OctantValue[i:i+t].count('+2'),
            -2: OctantValue[i:i+t].count('-2'), 3: OctantValue[i:i+t].count('+3'), -3: OctantValue[i:i+t].count('-3'),
            4: OctantValue[i:i+t].count('+4'), -4: OctantValue[i:i+t].count('-4')}
        h = h.append(j, ignore_index=True)
    frames = [fg, h]
    #append both dataframe in single one
    result = pd.concat(frames, axis=1)
    result.to_csv("octant_output.csv", index=False)

	


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)
	


from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)