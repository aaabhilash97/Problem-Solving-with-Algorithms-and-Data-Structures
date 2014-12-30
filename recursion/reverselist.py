def revlist(x,l=[]):
	if len(l)==len(x):
		return l
	l.append(x[-(len(l)+1)])
	return revlist(x,l)
print(revlist([1,23,4,4,6,7,8,3]))
