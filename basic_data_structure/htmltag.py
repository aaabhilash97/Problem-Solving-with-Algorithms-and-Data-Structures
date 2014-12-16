import re
def checkhtml(html):
	f=open(html,'r').read().split()
	htmltagso=re.findall(r'<\w+>',open(html,'r').read())
	htmltagsc=re.findall(r'</\w.+>',open(html,'r').read())
	buff=[]
	unbuff=[]
	for x in f:
		if x in htmltagso:
			buff.append(x)
		elif x in htmltagsc:
			try:
			 	buff.remove(x[0]+x[2:])
			except:
				print "improper tag"
				exit()
	if len(buff)>0:
		print "tag are improper",buff
	else :
		print "OK"
checkhtml("simplehtml.html")
