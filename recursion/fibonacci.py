def fib(n,res=[0,1]):
	if n==0:
		return [0]
	if n==1:
		return [0,1]
	if len(res)-1==n:
		return res
	else:
		res.append(res[len(res)-1]+res[len(res)-2])
		return fib(n,res)
print fib(6)
