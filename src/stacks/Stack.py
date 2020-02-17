# Copyright (C) 2020 Akash Nag
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#	
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#	
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



# Implementation of an array-based Stack
# Supported operations:
#	- Is Empty	O(1)
#	- Is Full	O(1)
#	- Push		O(1)
#	- Pop		O(1)
#	- Peek		O(1)
#	- Display	O(n)

class Stack:
	def __init__(self, n):
		self.capacity = n
		self.data = [0 for i in range(n)]
		self.top = -1

	def isEmpty(self):
		return(True if (self.top == -1) else False)

	def isFull(self):
		return(True if (self.top == self.capacity-1) else False)

	def push(self, v):
		if(self.isFull()):
			raise(Exception("Stack overflow"))
		else:
			self.top = self.top + 1
			self.data[self.top] = v
	
	def pop(self):
		if(self.isEmpty()):
			raise(Exception("Stack underflow"))
		else:
			v = self.data[self.top]
			self.top = self.top - 1
			return v
	
	def peek(self):
		if(self.isEmpty()):
			raise(Exception("Stack underflow"))
		else:
			v = self.data[self.top]
			return v
	
	def display(self):
		if(self.isEmpty()):
			print("Stack is empty")
		else:
			print("Stack contents:")
			for i in range(self.top, -1, -1):
				print(self.data[i])

def main():
	n = int(input("Enter stack capacity: "))
	stack = Stack(n)

	while(True):
		c = printMenu()
		if(c==1):
			v = int(input("Enter a value to push: "))
			stack.push(v)
		elif(c==2):
			v = stack.pop()
			print("Popped value: " + str(v))
		elif(c==3):
			stack.display()
		elif(c==4):
			return

def printMenu():
	c = 0
	while(c<1 or c>4):
		c = int(input("MENU\n----\n1. Push\n2. Pop\n3. Display\n4. Exit\nEnter choice: "))
		if(c<1 or c>4):
			print("Invalid choice! Try again...")
	
	return c

main()