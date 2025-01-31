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



# Implementation of a linked-list based Stack
# Supported operations:
#	- Is Empty	O(1)
#	- Is Full	O(1)
#	- Push		O(1)
#	- Pop		O(1)
#	- Peek		O(1)
#	- Display	O(n)

class Node:
	def __init__(self, v):
		self.data = v
		self.next = None

class LinkedStack:
	def __init__(self):
		self.top = None

	def push(self, v):
		temp = Node(v)
		temp.next = self.top
		self.top = temp

	def pop(self):
		if(self.top == None):
			raise(Exception("Stack underflow"))
		else:
			v = self.top.data
			self.top = self.top.next
			return v
	
	def peek(self):
		if(self.top == None):
			raise(Exception("Stack underflow"))
		else:
			return self.top.data
	
	def display(self):
		if(self.top == None):
			raise(Exception("Stack is empty"))
		else:
			print("Stack contents:")
			temp = self.top
			while(temp != None):
				print(temp.data)
				temp = temp.next

def main():
	stack = LinkedStack(10)

	stack.push(8)
	stack.push(2)
	stack.push(11)
	stack.push(14)
	stack.push(9)

	stack.pop()
	stack.pop()

	stack.display()

main()