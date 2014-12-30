from Node import *
class UnorderedList:
	def __init__(self):
		self.head = None
	def is_empty(self):
		return self.head == None
	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()
		return count
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()
		return found
	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()
		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
#__str__ METHOD
	def __str__(self):
		a=self.head
		l='['
		while a!=None:
			l=l+str(a.data)+' , '
			a=a.next
		l=l[0:-2]+']'
		return l
#Implement the remaining operations defined in the UnorderedList ADT (append, index,pop, insert).
# POP
	def pop(self):
		a=self.head
		p=a
		while a.next!=None:
			p=a
			a=a.next
		p.next=None
		return a.data
# APPEND
	def append(self,item):
		a=self.head
		while a.next!=None:
			a=a.next
		a.next=Node(item)
# INSERT
	def insert(self,item,pos):
		if pos==0:
			self.add(item)
			return
		a=self.head
		p=a
		while pos>0:
			p=a
			a=a.next
			pos-=1
		temp=Node(item)
		p.next=temp
		temp.next=a
# INDEX
	def index(self,item):
		a=self.head
		pos=0
		while a!=None:
			if a.data==item:
				return pos
			pos+=1
			a=a.next
# SLICE  WITH StART ND STOP
	def slice(self,start,stop):
		a=self.head
		while start>0 and a!=None:
			a=a.next
			start-=1
		st=a
		while stop>1 and a!=None:
			a=a.next
			stop-=1
		a.next=None
		ret=UnorderedList()
		ret.head=st
		return ret
class OrderedList:
	def __init__(self):
		self.head = None
	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.get_data() == item:
				found = True
			else:
				if current.get_data() > item:
					stop = True
				else:
					current = current.get_next()
		return found
	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.get_data() > item:
				stop = True
			else:
				previous = current
				current = current.get_next()
		temp = Node(item)
		if previous == None:
			temp.set_next(self.head)
			self.head = temp
		else:
			temp.set_next(current)
			previous.set_next(temp)
