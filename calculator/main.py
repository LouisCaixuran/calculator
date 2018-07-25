import wx
import re

class Stack(object):
    def __init__(self):
        self.items=[]
    def peak(self):
    	return self.items[len(self.items)-1]
    def push(self,x):
        return self.items.append(x)
    def pop(self):
        return self.items.pop()
    def isempty(self):
        return self.items==[]
    def size(self):
    	return len(self.items)


OPERATOR={
	'@':0,
	'+':1,
	'-':1,
	'*':2,
	'/':2
}


def startcal():
	parse=argparse.ArgumentParser(description="science calculator")
	parse.add_argument("formula",help="input math formula")
	args=parse.parse_args()

	print(args)

	calculate(args.formula)

def desparate(formula):
	return re.split('(\+|\-|\*|\/)',formula)

			 



def transfer(list):
	global OPERATOR
	operatorstack=Stack()
	operatorstack.push('@')
	suffix=[]

	for i in range(len(list)):
		if list[i][0].isdigit():
			suffix.append(list[i])
		else:
			while  OPERATOR[operatorstack.peak()]>=OPERATOR[list[i]]: 
				suffix.append(operatorstack.peak())
				operatorstack.pop()
			operatorstack.push(list[i])
	
	while operatorstack.peak()!= '@':
		suffix.append(operatorstack.peak())
		operatorstack.pop()
	
	return suffix

def calculate(formula):
	
	n=desparate(formula)
	suffix=transfer(n)
	i=0
	while i<=len(suffix):	
		i=0
		while not suffix[i] in ['+','-','*','/']:
			i=i+1
		
		
		suffix[i]=cal(suffix[i-2],suffix[i-1],suffix[i])
		
		del suffix[i-1],suffix[i-2]	

    
	ans=suffix[0]
	return ans

def  cal(a,b,action):
	a=int(a)
	b=int(b)
	if action=="+":
		return a+b
	if action=="-":
		return a-b
	if action == '*':
		return a*b
	if  action =='/':
		if b==0:
			return 0
		else:	
			return a/b


if __name__ == '__main__':
	a="12+30-5*8/2"
	print(a)
	print(desparate(a))
	print(transfer(desparate(a)))
	print(calculate(a))

	

