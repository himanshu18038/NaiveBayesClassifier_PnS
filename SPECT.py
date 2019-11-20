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
	for i in range(len(x)):
		l2=[]
		for j in range(0,2):
			l2.append(prob(x[i],y,j,0))
			l2.append(prob(x[i],y,j,1))
		l.append(l2)
	l2=[]
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


def calculate(s1,s2,l):
	num=1
	for i in range(len(s1)):
		a=int(s1[i])
		if(a==0):
			if(s2==0):
				n=0
			elif(s2==1):
				n=1
		elif(a==1):
			if(s2==0):
				n=2
			elif(s2==1):
				n=3
		num*=l[i][n]*1
	return num*0.5*1

def final_calculator(l12,l11,y):
	ans=[]
	i=0
	while(i<len(l12)):
		t2=calculate(l12[i],1,l11)
		t1=calculate(l12[i],0,l11)
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

data1=pd.read_csv("SPECTtrain.txt", sep=",", header=None)
data2=pd.read_csv("SPECTtest.txt",sep=",",header=None)
x1=matrixmaking(data1)
y1=classmaking(data1)
x2=matrixmaking(data2)
y2=classmaking(data2)
l1=conditionalprobs(x1,y1)
l2=test_files_calculator(x2)
ans=final_calculator(l2,l1,y1)
print("The accuracy of SPECT is: "+str(accuracy(y2,ans)))