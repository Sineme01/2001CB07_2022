import sys
import datetime 
start_time = datetime.datetime.now()

def scorecard():

	sys.stdout = open('Scorecard.txt','wt')
	f=open('team.txt',"r")
	a=f.readlines()
	f1=open("pak_inns1.txt","r")
	com1=f1.readlines()
	f2=open("india_inns2.txt","r")
	com2=f2.readlines()
	Array2=a[0].split(':')[1]
	Array1=a[2].split(':')[1]

	Array2_Name = a[0].split('(')[0][:-1]
	Array1_Name = a[2].split('(')[0][:-1]

	Array3 = Array2.split()
	Array2=Array2.split(',')
	for i in range(len(Array2)):
		if(Array2[i].endswith('\n')):
			Array2[i]=Array2[i][:-1]

	Array1=Array1.split(',')
	for i in range(len(Array1)):
		if(Array1[i].endswith('\n')):
			Array1[i]=Array1[i][:-1]
	dict_Array1Players={}
	dict_Array2Players={}
	for i in Array1:
		dict_Array1Players[i[1:]]=i[1:]
	for i in Array2:
		dict_Array2Players[i[1:]]=i[1:]
	if com1[0].split()[1] in Array3:
		temp = Array1_Name
		Array1_Name = Array2_Name
		Array2_Name = temp
		temp = dict_Array1Players
		dict_Array1Players = dict_Array2Players
		dict_Array2Players=temp
		temp = Array1
		Array1 = Array2
		Array2 = temp

	ls=[]
	lp=[]

	for i in com1[::2]:
		a=i.split(",")
		b=a[0]
		b=b.split('to')
		Array2bat=b[1][1:]
		ball,Array1Bowl=b[0].split(" ",1)
		Array1Bowl=Array1Bowl[:-1]
		p=b[0].split(" ",2)
		u=1
		if(Array2bat not in dict_Array2Players):
			lp.append(Array2bat)
		if(Array1Bowl not in dict_Array1Players):
			ls.append(Array1Bowl)
	for i in com2[::2]:
		a=i.split(",")
		b=a[0]
		b=b.split('to')
		Array1bat=b[1][1:]
		ball,Array2Bowl=b[0].split(" ",1)
		Array2Bowl=Array2Bowl[:-1]
		if(Array1bat not in dict_Array1Players):
				ls.append(Array1bat)
		if(Array2Bowl not in dict_Array2Players):
			lp.append(Array2Bowl)
	ls=set(ls)
	lp=set(lp)
	makei=[]
	makep=[]
	deli=[]
	delp=[]
    
	for j in ls:
		for i in dict_Array1Players:
			if(j.lower() in dict_Array1Players[i].lower()):
				makei.append([j,dict_Array1Players[i]])
				deli.append(dict_Array1Players[i])
	for j in lp:
		for i in dict_Array2Players:
			if(j.lower() in dict_Array2Players[i].lower()):
				makep.append([j,dict_Array2Players[i]])
				delp.append(dict_Array2Players[i])

	for j in deli:
		del dict_Array1Players[j]
	for j in delp:
		del dict_Array2Players[j]
	for i,j in makei:
		dict_Array1Players[i]=j
	for i,j in makep:
		dict_Array2Players[i]=j
	BatterArray2=[]
	BatterArray21=[]
	BowlerArray1=[]
	BowlerArray11=[]
	BatterArray1=[]
	BatterArray11=[]
	BowlerArray2=[]
	BowlerArray21=[]
	OutArray2={}
	for i in dict_Array2Players:
		OutArray2[i]="not out"
	OutArray1={}
	for i in dict_Array1Players:
		OutArray1[i]="not out"
	BatterArray2Run={}
	for i in dict_Array2Players:
		BatterArray2Run[i]=0
	BatterArray1Run={}
	for i in dict_Array1Players:
		BatterArray1Run[i]=0
	BatterArray2Ball={}
	for i in dict_Array2Players:
		BatterArray2Ball[i]=0
	BatterArray1Ball={}
	for i in dict_Array1Players:
		BatterArray1Ball[i]=0
	BatterArray24s={}
	for i in dict_Array2Players:
		BatterArray24s[i]=0
	BatterArray14s={}
	for i in dict_Array1Players:
		BatterArray14s[i]=0
	BatterArray26s={}
	for i in dict_Array2Players:
		BatterArray26s[i]=0
	BatterArray16s={}
	for i in dict_Array1Players:
		BatterArray16s[i]=0



	Array2b=0;Array2lb=0;Array2w=0;Array2nb=0;Array2p=0
	Array1b=0;Array1lb=0;Array1w=0;Array1nb=0;Array1p=0
	Array2powerRun=0;Array1powerRun=0
	Array1BowlerOver={}
	for i in dict_Array1Players:
		Array1BowlerOver[i]=0
	Array2BowlerOver={}
	for i in dict_Array2Players:
		Array2BowlerOver[i]=0
	Array1BowlerMaiden={}
	for i in dict_Array1Players:
		Array1BowlerMaiden[i]=0
	Array2BowlerMaiden={}
	for i in dict_Array2Players:
		Array2BowlerMaiden[i]=0
	Array2BowlerRun={}
	for i in dict_Array2Players:
		Array2BowlerRun[i]=0
	Array1BowlerRun={}
	for i in dict_Array1Players:
		Array1BowlerRun[i]=0
	Array2BowlerWicket={}
	for i in dict_Array2Players:
		Array2BowlerWicket[i]=0
	Array1BowlerWicket={}
	for i in dict_Array1Players:
		Array1BowlerWicket[i]=0
	Array2BowlerNb={}
	for i in dict_Array2Players:
		Array2BowlerNb[i]=0
	Array1BowlerNb={}
	for i in dict_Array1Players:
		Array1BowlerNb[i]=0
	Array2BowlerWd={}
	for i in dict_Array2Players:
		Array2BowlerWd[i]=0
	Array1BowlerWd={}
	for i in dict_Array1Players:
		Array1BowlerWd[i]=0
	fallArray1=[]
	fallArray2=[]
	totalrun1=0
	totalrun2=0
	wicket1=0
	wicket2=0
	d_run={'1':1,'2':2,'3':3,'four':4,'six':6,'five':5}

	prev='0'
	pt=0
	u=0
	flag=0


	for i in com1[::2]:
		a=i.split(",")
		b=a[0]
		b=b.split('to')
		Array2bat=b[1][1:]
		ball,Array1Bowl=b[0].split(" ",1)
		Array1Bowl=Array1Bowl[:-1]
		p=b[0].split(" ",2)
		u=1
		if(dict_Array2Players[Array2bat] not in BatterArray21):
			BatterArray21.append(dict_Array2Players[Array2bat])
			BatterArray2.append(Array2bat)
		if(dict_Array1Players[Array1Bowl] not in BowlerArray11):
			BowlerArray11.append(dict_Array1Players[Array1Bowl])
			BowlerArray1.append(Array1Bowl)
		if(prev!=ball):
			Array1BowlerOver[Array1Bowl]+=1
		
		prev=ball
		ch=a[1]
		ch=ch.split(' ',1)
		ya=ch[1].split(" ")
		wa=ch[1].split(" ",1)
		if(ya[0].lower()=='1' and ya[1].lower()=='run'):
			Array1BowlerRun[Array1Bowl]+=1
			BatterArray2Ball[Array2bat]+=1
			totalrun1+=1
			BatterArray2Run[Array2bat]+=1
		elif(ya[0].lower()=='2' and ya[1].lower()=='runs'):
			Array1BowlerRun[Array1Bowl]+=2
			totalrun1+=2
			BatterArray2Ball[Array2bat]+=1
			BatterArray2Run[Array2bat]+=2
		elif(ya[0].lower()=='3' and ya[1].lower()=='runs'):
			Array1BowlerRun[Array1Bowl]+=3
			totalrun1+=3    
			BatterArray2Ball[Array2bat]+=1
			BatterArray2Run[Array2bat]+=3
		elif(ya[0].lower()=='four'):
		
			Array1BowlerRun[Array1Bowl]+=4
			totalrun1+=4
			BatterArray24s[Array2bat]+=1
			BatterArray2Ball[Array2bat]+=1
			BatterArray2Run[Array2bat]+=4
		elif(ya[0].lower()=='six'):
	
			Array1BowlerRun[Array1Bowl]+=6
			totalrun1+=6
			BatterArray26s[Array2bat]+=1
			BatterArray2Ball[Array2bat]+=1
			BatterArray2Run[Array2bat]+=6
		elif(ya[0].lower()=='byes'):
			o=a[2].split(' ')
			totalrun1+=d_run[o[1].lower()]
			BatterArray2Ball[Array2bat]+=1
			Array2b+=d_run[o[1].lower()]
		elif(ya[0].lower()=='leg'):
			o=a[2].split(' ')
			totalrun1+=d_run[o[1].lower()]
			BatterArray2Ball[Array2bat]+=1
			Array2lb+=d_run[o[1].lower()]
		elif(ya[0].lower()=='no'):
			if(ya[1]=='ball'):
				totalrun1+=1
				Array2nb+=1
			else:
				BatterArray2Ball[Array2bat]+=1
		elif(ya[0].lower()=='out'):
			g=wa[1].split('!!')[0]
			g=g.split(' ',2)
			wicket1+=1
			if(len(g)!=1):
				OutArray2[Array2bat]=f'c {g[-1]} b {Array1Bowl}'
			else:
				x=g[-1].lower()
				if('lbw'==x):
					OutArray2[Array2bat]=f'{x} b {Array1Bowl}'
				else:
					OutArray2[Array2bat]=f'b {Array1Bowl}'
			Array1BowlerWicket[Array1Bowl]+=1
			fallArray2.append(f'{totalrun1}-{wicket1} ({dict_Array2Players[Array2bat]},{ball})')
			BatterArray2Ball[Array2bat]+=1
		elif((ya[0].lower()=='wide') or ((ya[0].lower()=='1' or ya[0].lower()=='2' or ya[0].lower()=='3') and ('wide' in ya[1].lower()))):
			
			
			if(ya[0].lower()=='wide'):
					Array2w+=1
					totalrun1+=1
					Array1BowlerWd[Array1Bowl]+=1
					Array1BowlerRun[Array1Bowl]+=1
			else:
				Array2w+=int(ya[0])
				totalrun1+=int(ya[0])
				Array1BowlerWd[Array1Bowl]+=int(ya[0])
				Array1BowlerRun[Array1Bowl]+=int(ya[0])
		
			
		
		if(ball.endswith('.6')):
			if(totalrun1==pt):
				Array1BowlerMaiden[Array1Bowl]+=1
			pt=totalrun1
		
		if(ball=='5.6'):
			Array2powerRun=totalrun1
	ap= Array2_Name +' Innings'
	print(ap.ljust(85),end=" ")
	if(ball.endswith('.6')):
		ball=ball[0]
	print(f'{totalrun1}-{wicket1}({ball} Ov)')
	prt=['Batter','R','B','4s','6s','SR']

	print(prt[0].ljust(28),end=" ")
	print(" ".ljust(38),end=" ")
	print(prt[1].ljust(7),end=" ")
	print(prt[2].ljust(6),end="")
	print(prt[3].ljust(6),end=" ")
	print(prt[4].ljust(7),end=" ")
	print(prt[5])

	strike_Array2={}


	for i in BatterArray2:
		strike_Array2[i]=round((BatterArray2Run[i]/BatterArray2Ball[i])*100,2)
	c=0
	for i in BatterArray2:
		print(dict_Array2Players[i].ljust(28),end=" ")
		print(OutArray2[i].ljust(38),end=" ")
		print(str(BatterArray2Run[i]).ljust(7),end=" ")
		print(str(BatterArray2Ball[i]).ljust(6),end="")
		print(str(BatterArray24s[i]).ljust(6),end=" ")
		print(str(BatterArray26s[i]).ljust(4),end=" ")
		print(str(strike_Array2[i]))

	print("Extras".ljust(70),end=" ")
	print(str(Array2b+Array2lb+Array2w+Array2nb+Array2p)+f'(b {Array2b}, lb {Array2lb}, w {Array2w}, nb {Array2nb}, p {Array2p})')
	print("Total".ljust(70),end=" ")
	print(str(totalrun1)+f'({wicket1} wkts, {ball} Ov)')
	if(len(BatterArray2)!=11):
		print("Did not bat".ljust(20),end=" ")
	c=0
	for i in dict_Array2Players:
		if(i not in BatterArray2):
			if(c==0):
				print(dict_Array2Players[i],end="")
			else:
				print(',',dict_Array2Players[i],end="")
			c+=1
	if(c>0):
		print("")




	print("Fall of Wickets")
	c=0
	s=""
	for i in fallArray2[:-1]:
		s+=i
		s+=", "
	s+=fallArray2[-1]

	for i in s:
		if(c==99):
			c=0
			print("")
		print(i,end="")
		c+=1
	print("")
	heading=['Bowler','O','M','R','W','NB','WD','ECO']
	print(heading[0].ljust(60),end=" ")
	print(heading[1].ljust(5),end=" ")
	print(heading[2].ljust(5),end="")
	print(heading[3].ljust(5),end=" ")
	print(heading[4].ljust(5),end=" ")
	print(heading[5].ljust(4),end=" ")
	print(heading[6].ljust(5),end=" ")
	print(heading[7])
	Array1BowlerEco={}
	for i in BowlerArray1:
		x=Array1BowlerOver[i]
		d=x//6
		di=x%6

		if(di!=0):
			d=d+(di/6)
		
		Array1BowlerEco[i]=round(Array1BowlerRun[i]/d,2)

	for i in BowlerArray1:
		print(dict_Array1Players[i].ljust(60),end=" ")
		x=Array1BowlerOver[i]
		d=str(x//6)
		di=x%6
		if(di!=0):
			d+=('.'+str(di))

		print(d.ljust(5),end=" ")
		print(str(Array1BowlerMaiden[i]).ljust(4),end=" ")
		print(str(Array1BowlerRun[i]).ljust(5),end=" ")
		print(str(Array1BowlerWicket[i]).ljust(5),end=" ")
		print(str(Array1BowlerNb[i]).ljust(4),end=" ")
		print(str(Array1BowlerWd[i]).ljust(5),end=" ")
		print(str(Array1BowlerEco[i]))

	print('Powerplays'.ljust(46),end=" ")
	print('Overs'.ljust(46),end=" ")
	print("Runs")
	print("Mandatory".ljust(46),end=" ")
	print("0.1-6".ljust(47),end=" ")
	print(Array2powerRun)






	print('\n')

	BatterArray2=[]
	BowlerArray1=[]
	BatterArray1=[]
	BowlerArray2=[]
	OutArray2={}
	for i in dict_Array2Players:
		OutArray2[i]="not out"
	OutArray1={}
	for i in dict_Array1Players:
		OutArray1[i]="not out"
	BatterArray2Run={}
	for i in dict_Array2Players:
		BatterArray2Run[i]=0
	BatterArray1Run={}
	for i in dict_Array1Players:
		BatterArray1Run[i]=0
	BatterArray2Ball={}
	for i in dict_Array2Players:
		BatterArray2Ball[i]=0
	BatterArray1Ball={}
	for i in dict_Array1Players:
		BatterArray1Ball[i]=0
	BatterArray24s={}
	for i in dict_Array2Players:
		BatterArray24s[i]=0
	BatterArray14s={}
	for i in dict_Array1Players:
		BatterArray14s[i]=0
	BatterArray26s={}
	for i in dict_Array2Players:
		BatterArray26s[i]=0
	BatterArray16s={}
	for i in dict_Array1Players:
		BatterArray16s[i]=0



	Array2b=0;Array2lb=0;Array2w=0;Array2nb=0;Array2p=0
	Array1b=0;Array1lb=0;Array1w=0;Array1nb=0;Array1p=0
	Array2powerRun=0;Array1powerRun=0
	Array1BowlerOver={}
	for i in dict_Array1Players:
		Array1BowlerOver[i]=0
	Array2BowlerOver={}
	for i in dict_Array2Players:
		Array2BowlerOver[i]=0
	Array1BowlerMaiden={}
	for i in dict_Array1Players:
		Array1BowlerMaiden[i]=0
	Array2BowlerMaiden={}
	for i in dict_Array2Players:
		Array2BowlerMaiden[i]=0
	Array2BowlerRun={}
	for i in dict_Array2Players:
		Array2BowlerRun[i]=0
	Array1BowlerRun={}
	for i in dict_Array1Players:
		Array1BowlerRun[i]=0
	Array2BowlerWicket={}
	for i in dict_Array2Players:
		Array2BowlerWicket[i]=0
	Array1BowlerWicket={}
	for i in dict_Array1Players:
		Array1BowlerWicket[i]=0
	Array2BowlerNb={}
	for i in dict_Array2Players:
		Array2BowlerNb[i]=0
	Array1BowlerNb={}
	for i in dict_Array1Players:
		Array1BowlerNb[i]=0
	Array2BowlerWd={}
	for i in dict_Array2Players:
		Array2BowlerWd[i]=0
	Array1BowlerWd={}
	for i in dict_Array1Players:
		Array1BowlerWd[i]=0
	fallArray1=[]
	fallArray2=[]
	totalrun1=0
	totalrun2=0
	wicket1=0
	wicket2=0
	d_run={'1':1,'2':2,'3':3,'four':4,'six':6,'five':5}
	prev='0'
	pt=0
	u=0

	for i in com2[::2]:
		a=i.split(",")
		b=a[0]
		b=b.split('to')
		Array1bat=b[1][1:]
		ball,Array2Bowl=b[0].split(" ",1)
		Array2Bowl=Array2Bowl[:-1]
		p=b[0].split(" ",2)
		u=1



		if(dict_Array1Players[Array1bat] not in BatterArray11):
			BatterArray11.append(dict_Array1Players[Array1bat])
			BatterArray1.append(Array1bat)
		if(dict_Array2Players[Array2Bowl] not in BowlerArray21):
			BowlerArray21.append(dict_Array2Players[Array2Bowl])
			BowlerArray2.append(Array2Bowl)
		if(prev!=ball):
			Array2BowlerOver[Array2Bowl]+=1
		
		prev=ball
		ch=a[1]
		ch=ch.split(' ',1)
		ya=ch[1].split(" ")
		wa=ch[1].split(" ",1)
		if(ya[0].lower()=='1' and ya[1].lower()=='run'):
			Array2BowlerRun[Array2Bowl]+=1
			BatterArray1Ball[Array1bat]+=1
			totalrun1+=1
			BatterArray1Run[Array1bat]+=1
		elif(ya[0].lower()=='2' and ya[1].lower()=='runs'):
			Array2BowlerRun[Array2Bowl]+=2
			totalrun1+=2
			BatterArray1Ball[Array1bat]+=1
			BatterArray1Run[Array1bat]+=2
		elif(ya[0].lower()=='3' and ya[1].lower()=='runs'):
			Array2BowlerRun[Array2Bowl]+=3
			totalrun1+=3    
			BatterArray1Ball[Array1bat]+=1
			BatterArray1Run[Array1bat]+=3
		elif(ya[0].lower()=='four'):
		
			Array2BowlerRun[Array2Bowl]+=4
			totalrun1+=4
			BatterArray14s[Array1bat]+=1
			BatterArray1Ball[Array1bat]+=1
			BatterArray1Run[Array1bat]+=4
		elif(ya[0].lower()=='six'):
	
			Array2BowlerRun[Array2Bowl]+=6
			totalrun1+=6
			BatterArray16s[Array1bat]+=1
			BatterArray1Ball[Array1bat]+=1
			BatterArray1Run[Array1bat]+=6
		elif(ya[0].lower()=='byes'):
			o=a[2].split(' ')
			totalrun1+=d_run[o[1].lower()]
			BatterArray1Ball[Array1bat]+=1
			Array1b+=d_run[o[1].lower()]
		elif(ya[0].lower()=='leg'):
			o=a[2].split(' ')
			totalrun1+=d_run[o[1].lower()]
			BatterArray1Ball[Array1bat]+=1
			Array1lb+=d_run[o[1].lower()]
		elif(ya[0].lower()=='no'):
			if(ya[1]=='ball'):
				Array1nb+=1
				totalrun2+=1
			else:
				BatterArray1Ball[Array1bat]+=1
		elif(ya[0].lower()=='out'):
			g=wa[1].split('!!')[0]
			
			g=g.split(' ',2)
			wicket1+=1
			if(len(g)!=1):
				OutArray1[Array1bat]=f'c {g[-1]} b {Array2Bowl}'
			else:
				x=g[-1].lower()
				if('lbw'==x):
					OutArray1[Array1bat]=f'{x} b {Array2Bowl}'
				else:
					OutArray1[Array1bat]=f'b {Array2Bowl}'
			Array2BowlerWicket[Array2Bowl]+=1
			fallArray1.append(f'{totalrun1}-{wicket1} ({dict_Array1Players[Array1bat]},{ball})')
			BatterArray1Ball[Array1bat]+=1
		elif((ya[0].lower()=='wide') or ((ya[0].lower()=='1' or ya[0].lower()=='2' or ya[0].lower()=='3') and ('wide' in ya[1].lower()))):
			
			
			if(ya[0].lower()=='wide'):
					Array1w+=1
					totalrun1+=1
					Array2BowlerWd[Array2Bowl]+=1
					Array2BowlerRun[Array2Bowl]+=1
			else:
				Array1w+=int(ya[0])
				totalrun1+=int(ya[0])
				Array2BowlerWd[Array2Bowl]+=int(ya[0])
				Array2BowlerRun[Array2Bowl]+=int(ya[0])
		
			
		
		if(ball.endswith('.6')):
			if(totalrun1==pt):
				Array2BowlerMaiden[Array2Bowl]+=1
			pt=totalrun1
		
		if(ball=='5.6'):
			Array1powerRun=totalrun1
	ap= Array1_Name +' Innings'
	print(ap.ljust(85),end=" ")
	if(ball.endswith('.6')):
		ball=ball[0]
	print(f'{totalrun1}-{wicket1}({ball} Ov)')
	prt=['Batter','R','B','4s','6s','SR']

	print(prt[0].ljust(28),end=" ")
	print(" ".ljust(38),end=" ")
	print(prt[1].ljust(7),end=" ")
	print(prt[2].ljust(6),end="")
	print(prt[3].ljust(6),end=" ")
	print(prt[4].ljust(7),end=" ")
	print(prt[5])

	strike_Array1={}


	for i in BatterArray1:
		strike_Array1[i]=round((BatterArray1Run[i]/BatterArray1Ball[i])*100,2)
	c=0
	for i in BatterArray1:
		print(dict_Array1Players[i].ljust(28),end=" ")
		print(OutArray1[i].ljust(38),end=" ")
		print(str(BatterArray1Run[i]).ljust(7),end=" ")
		print(str(BatterArray1Ball[i]).ljust(6),end="")
		print(str(BatterArray14s[i]).ljust(6),end=" ")
		print(str(BatterArray16s[i]).ljust(4),end=" ")
		print(str(strike_Array1[i]))

	print("Extras".ljust(70),end=" ")
	print(str(Array1b+Array1lb+Array1w+Array1nb+Array1p)+f'(b {Array1b}, lb {Array1lb}, w {Array1w}, nb {Array1nb}, p {Array1p})')
	print("Total".ljust(70),end=" ")
	print(str(totalrun1)+f'({wicket1} wkts, {ball} Ov)')
	if(len(BatterArray1)!=11):
		print("Did not bat".ljust(20),end=" ")
	c=0
	for i in dict_Array1Players:
		if(i not in BatterArray1):
			if(c==0):
				print(dict_Array1Players[i],end="")
			else:
				print(',',dict_Array1Players[i],end="")
			c+=1
	if(c>0):
		print("")

	print("Fall of Wickets")
	c=0
	s=""
	for i in fallArray1[:-1]:
		s+=i
		s+=", "
	s+=fallArray1[-1]

	for i in s:
		if(c==99):
			c=0
			print("")
		print(i,end="")
		c+=1
	print("")
	heading=['Bowler','O','M','R','W','NB','WD','ECO']
	print(heading[0].ljust(60),end=" ")
	print(heading[1].ljust(5),end=" ")
	print(heading[2].ljust(5),end="")
	print(heading[3].ljust(5),end=" ")
	print(heading[4].ljust(5),end=" ")
	print(heading[5].ljust(4),end=" ")
	print(heading[6].ljust(5),end=" ")
	print(heading[7])
	Array2BowlerEco={}
	for i in BowlerArray2:
		x=Array2BowlerOver[i]
		d=x//6
		di=x%6

		if(di!=0):
			d=d+(di/6)
		
		Array2BowlerEco[i]=round(Array2BowlerRun[i]/d,2)

	for i in BowlerArray2:
		print(dict_Array2Players[i].ljust(60),end=" ")
		x=Array2BowlerOver[i]
		d=str(x//6)
		di=x%6
		if(di!=0):
			d+=('.'+str(di))

		print(d.ljust(5),end=" ")
		print(str(Array2BowlerMaiden[i]).ljust(4),end=" ")
		print(str(Array2BowlerRun[i]).ljust(5),end=" ")
		print(str(Array2BowlerWicket[i]).ljust(5),end=" ")
		print(str(Array2BowlerNb[i]).ljust(4),end=" ")
		print(str(Array2BowlerWd[i]).ljust(5),end=" ")
		print(str(Array2BowlerEco[i]))

	print('Powerplays'.ljust(46),end=" ")
	print('Overs'.ljust(46),end=" ")
	print("Runs")
	print("Mandatory".ljust(46),end=" ")
	print("0.1-6".ljust(47),end=" ")
	print(Array1powerRun)





from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()

end_time = datetime.datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))