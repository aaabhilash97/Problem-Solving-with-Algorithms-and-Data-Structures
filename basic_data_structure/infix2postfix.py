from Stack import *
def infix_to_postfix(infix_expr):
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	op_stack = Stack()
	n=0
	postfix_list = []
	token_list = infix_expr.split(" ")
	for token in token_list:
		if token not in "+-*/()":
			postfix_list.append(token)
		elif token == '(':
			n+=1
			op_stack.push(token)
		elif token == ')':
			n-=1
			top_token = op_stack.pop()
			while top_token != '(':
				postfix_list.append(top_token)
				top_token = op_stack.pop()
		else:
			while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
				postfix_list.append(op_stack.pop())
			op_stack.push(token)
	while not op_stack.is_empty():
		postfix_list.append(op_stack.pop())
	if n!=0:
		print "Not balanced"
		return None
	return " ".join(postfix_list)
