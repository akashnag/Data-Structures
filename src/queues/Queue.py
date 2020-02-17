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



# Implementation of an array-based Queue
# Supported operations:
#	- Is Empty	O(1)
#	- Is Full	O(1)
#	- Enqueue	O(1)
#	- Dequeue	O(1)
#	- Display	O(n)

class Queue:
	def __init__(self, n):
		self.capacity = n
		self.data = [0 for i in range(n)]
		self.front = -1
		self.rear = -1

	def isEmpty(self):
		return(True if (self.front == -1) else False)

	def isFull(self):
		return(True if (self.rear == self.capacity-1) else False)

	def enqueue(self, v):
		if(self.isFull()):
			raise(Exception("Queue overflow"))
		else:
			self.rear = self.rear + 1
			self.data[self.rear] = v
			if(self.front == -1):
				self.front = self.front + 1
	
	def dequeue(self):
		if(self.isEmpty()):
			raise(Exception("Queue underflow"))
		else:
			v = self.data[self.front]
			self.front = self.front + 1
			if(self.front > self.rear):
				self.front = -1
				self.rear = -1
			return v
	
	def display(self):
		if(self.isEmpty()):
			print("Queue is empty")
		else:
			print("Queue contents:")
			for i in range(self.front, self.rear+1):
				print(self.data[i])

def main():
	n = int(input("Enter queue capacity: "))
	queue = Queue(n)

	while(True):
		c = printMenu()
		if(c==1):
			v = int(input("Enter a value to enqueue: "))
			queue.enqueue(v)
		elif(c==2):
			v = queue.dequeue()
			print("Retrieved value: " + str(v))
		elif(c==3):
			queue.display()
		elif(c==4):
			return

def printMenu():
	c = 0
	while(c<1 or c>4):
		c = int(input("MENU\n----\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter choice: "))
		if(c<1 or c>4):
			print("Invalid choice! Try again...")
	
	return c

main()