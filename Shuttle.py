def func(x,y):
	a=y[0]
	n1=0
	n2=0
	for i in range(len(x)):
		if(x[i][0]=='1'):
			n1+=1
		else:
			n2+=1
	prob1=1
	prob2=1
	for i in range(1,len(y)):
		xp=0
		xn=0
		b=y[i]
		for j in range(len(x)):
			if(x[j][i]=='*'):
				xp+=1
				xn+=1
			elif(x[j][i]==b):
				if(x[j][0]==a):
					xp+=1
				else:
					xn+=1
		prob1*=(xp/n1)
		prob2*=(xn/n2)
	if(prob1==0 and prob2==0):
		return 0
	if(prob1>prob2):
		if('1'==y[0]):
			return 1
		else:
			return 0
	else:
		if('1'==y[0]):
			return 0
		else:
			return 1

f1=open('shuttle-landing-control.txt')
data=[]
a=f1.readlines()
for i in a:
	data.append(i.split(','))
l1=[]
for i in range(len(data)):
	x1=data[0:i]+data[i+1:]
	x2=data[i]
	l1.append(func(x1,x2))
print("The Accuracy of Shuttle is: "+str(sum(l1)*100/len(data)))