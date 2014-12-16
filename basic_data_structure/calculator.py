from infix2postfix import *
import sys
x=list()
q=[]
try:
	q=(infix_to_postfix("( 1 + 2 ) + ( 12 * 3 ) * 6")).split()
except:
	print "improper parentheses"
	exit()
for e in q:
	if e not in " +-*/":
		x.append(int(e))
	elif  e!=" ":
		x.append(e)
i=0
while len(x)>2:
	if x[i]=="+":
		x[i-2]=x[i-2]+x.pop(i-1)
		del x[i-1]
		i-=1
	elif x[i]=="*":
                x[i-2]=x[i-2]*x.pop(i-1)
                del x[i-1]
		i-=1
	elif x[i]=="-":
                x[i-2]=x[i-2]-x.pop(i-1)
                del x[i-1]
	else:i+=1
print x[0]
