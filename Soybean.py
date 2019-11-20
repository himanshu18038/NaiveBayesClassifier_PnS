def func(x,y):
	a=y[-1][0:-1]
	n1=0
	n2=0
	n3=0
	n4=0
	for i in range(len(x)):
		if(x[i][-1][0:-1]=='D1'):
			n1+=1
		elif(x[i][-1][0:-1]=='D2'):
			n2+=1
		elif(x[i][-1][:-1]=='D3'):
			n3+=1
		elif(x[i][-1][0:-1]=='D4'):
			n4+=1
	prob1=1
	prob2=1
	prob3=1
	prob4=1
	for i in range(1,len(y)):
		x1=0
		x2=0
		x3=0
		x4=0
		b=y[i]
		for j in range(len(x)):
			if(x[j][i]==b):
				if(x[j][-1][0:-1]=="D1"):
					x1+=1
				elif(x[j][-1][:-1]=="D2"):
					x2+=1
				elif(x[j][-1][:-1]=="D3"):
					x3+=1
				elif(x[j][-1][:-1]=="D4"):
					x4+=1
		prob1*=(x1/n1)
		prob2*=(x2/n2)
		prob3*=(x3/n1)
		prob4*=(x4/n2)
	if prob1==prob2 and prob3==prob4:
		return 0
	else:
		if(max(prob1,prob2,prob3,prob4)==prob1 and a=="D1"):
			return 1
		elif(max(prob1,prob2,prob3,prob4)==prob2 and a=="D2"):
			return 1
		elif(max(prob1,prob2,prob3,prob4)==prob3 and a=="D3"):
			return 1
		elif(max(prob1,prob2,prob3,prob4)==prob4 and a=="D4"):
			return 1
		else:
			return 0

f1=open('soybean-small.txt')
data=[]
a=f1.readlines()
for i in a:
	data.append(i.split(','))
l1=[]
for i in range(len(data)):
	x1=data[0:i]+data[i+1:]
	x2=data[i]
	l1.append(func(x1,x2))
print("The Accuracy of Soybean is: "+str(sum(l1)*100/len(data)))