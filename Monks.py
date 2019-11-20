import pandas as pd

def classmaking(data):
	return data.iloc[:,0].values.tolist()

def matrixmaking(data):
	t=[]
	for i in range(1,len(data.columns)):
		x=data.iloc[:,i].values
		x=x.tolist()
		t.append(x)
	return t

def prob(x,y,s1,s2):
	count1,count2=0,0
	for i in range(len(x)):
		if(x[i]==s1):
			if(y[i]==s2):
				count1+=1
	for i in range(len(y)):
		if(y[i]==s2 and 1==1):
			count2+=1
	return count1/count2


def conditionalprobs(x,y):
	l=[]
	l2=[]
	for i in range(1,4):
		l2.append(prob(x[0],y,i,0))
		l2.append(prob(x[0],y,i,1))	
	l.append(l2)
	
	l2=[]
	for i in range(1,4):
		l2.append(prob(x[1],y,i,0))
		l2.append(prob(x[1],y,i,1))	
	l.append(l2)

	l2=[]
	for i in range(1,3):
		l2.append(prob(x[2],y,i,0))
		l2.append(prob(x[2],y,i,1))	
	l.append(l2)

	l2=[]
	for i in range(1,4):
		l2.append(prob(x[3],y,i,0))
		l2.append(prob(x[3],y,i,1))	
	l.append(l2)

	l2=[]
	for i in range(1,5):
		l2.append(prob(x[4],y,i,0))
		l2.append(prob(x[4],y,i,1))	
	l.append(l2)

	l2=[]
	for i in range(1,3):
		l2.append(prob(x[5],y,i,0))
		l2.append(prob(x[5],y,i,1))	
	l.append(l2)
	return l

def test_files_calculator(x12):
	l=[]
	count=0
	for i in range(len(x12[0])):
		count+=1
		b=stringmaker(i,x12)
		l.append(b)
	return l

def stringmaker(a,x12):
	s=''
	for i in range(len(x12)-1):
		s+=str(x12[i][a])
	return s

def yprob(s,l):
	count1=0
	for i in range(len(l)):
		if(l[i]==s):
			count1+=1
	ans=count1/len(l)
	return ans


def calculate(y,s1,s2,l):
	num=1
	for i in range(len(s1)):
		a=int(s1[i])
		if(0<=i<=3 and i!=2):
			if(a==1):
				if(s2==0):
					n=0
				elif(s2==1):
					n=1
			elif(a==2):
				if(s2==0):
					n=2
				elif(s2==1):
					n=3
			elif(a==3):
				if(s2==0):
					n=4
				elif(s2==1):
					n=5
		elif i==2 or i==5:
			if(a==1):
				if(s2==0):
					n=0
				elif(s2==1):
					n=1
			elif(a==2):
				if(s2==0):
					n=2
				elif(s2==1):
					n=3
		else:
			if(a==1):
				if(s2==0):
					n=0
				elif(s2==1):
					n=1
			elif(a==2):
				if(s2==0):
					n=2
				elif(s2==1):
					n=3
			elif(a==3):
				if(s2==0):
					n=4
				elif(s2==1):
					n=5
			elif(a==4):
				if(s2==0):
					n=6
				elif(s2==1):
					n=7
		num*=l[i][n]*1
	return num*yprob(s2,y)*1

def final_calculator(l12,l11,y):
	ans=[]
	i=0
	while(i<len(l12)):
		t2=calculate(y,l12[i],1,l11)
		t1=calculate(y,l12[i],0,l11)
		if(t2<=t1):
			ans.append(0)
		else:
			ans.append(1)
		i+=1
	return ans

def accuracy(y,ans):
	count=0
	for i in range(len(y)):
		if(ans[i]==y[i]):
			count+=1
	return count*100/len(y)

for i in range(1,4):
	f=0
	if(i==1):
		data1=pd.read_csv("monks-1train.txt", sep=" ", header=None)
		data2=pd.read_csv("monks-1test.txt",sep=" ",header=None)
		f=1
	elif(i==2):
		data1=pd.read_csv("monks-2train.txt", sep=" ", header=None)
		data2=pd.read_csv("monks-2test.txt",sep=" ",header=None)
		f=1
	elif(i==3):
		data1=pd.read_csv("monks-3train.txt", sep=" ", header=None)
		data2=pd.read_csv("monks-3test.txt",sep=" ",header=None)
		f=1
	if(f==1):
		x1=matrixmaking(data1)
		y1=classmaking(data1)
		x2=matrixmaking(data2)
		y2=classmaking(data2)
		l1=conditionalprobs(x1,y1)
		l2=test_files_calculator(x2)
		ans=final_calculator(l2,l1,y1)
		print("The accuracy of Monks-"+str(i)+" is: " + str(accuracy(y2,ans)))