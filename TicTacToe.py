def func(x,y):
	l=[]
	pos=0
	neg=0
	for i in range(len(x)):
		for j in range(len(x[0])):
			if('positive' in x[i][-1]):
				pos+=1
			else:
				neg+=1
	xp=0
	xn=0
	op=0
	on=0
	bp=0
	bn=0
	for i in range(len(x)):
		l2=[]
		for j in range(len(x[0])):
			if(x[i][j]=='x'):
				if('positive'==x[9][:-1]):
					xp+=1
				else:
					xn+=1
			elif(x[i][j]=='o'):
				if('positive'==x[9][:-1]):
					op+=1
				else:
					on+=1
			elif(x[i][j]=='b'):
				if('positive'==x[9][:-1]):
					bp+=1
				else:
					bn+=1
	probp=1
	probn=1
	for i in range(len(y[0])-1):
		if(y[0][i]=='x'):
			probp*=xp/pos
			probn*=xn/neg
		elif(y[0][i]=='o'):
			probp*=op/pos
			probn*=on/neg
		elif(y[0][i]=='b'):
			probp*=bp/pos
			probn*=bn/neg
	probp*=pos/(pos+neg)
	probn*=neg/(pos+neg)
	if(probp>probn):
		if('positive'==y[9][:-1]):
			return 1
		else:
			return 0
	else:
		if('positive'==y[9][:-1]):
			return 0
		else:
			return 1

f1=open('tic-tac-toe.txt')
data=[]
a=f1.readlines()
for i in a:
	data.append(i.split(','))
l1=[]
for i in range(len(data)):
	x1=data[0:i]+data[i+1:]
	x2=data[i]
	l1.append(func(x1,x2))
print("The Accuracy of TicTacToe is: "+str(sum(l1)*100/len(data)))