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



# Implementation of a linked-list based Queue
# Supported operations:
#	- Is Empty	O(1)
#	- Enqueue	O(1)
#	- Dequeue	O(1)
#	- Display	O(n)

class Node:
	def __init__(self, v):
		self.data = v
		self.next = None

class LinkedQueue:
	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return(True if (self.head == None) else False)

	def enqueue(self, v):
		node = Node(v)
		if(self.tail == None):
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
	
	def dequeue(self):
		if(self.isEmpty()):
			raise(Exception("Queue underflow"))
		else:
			v = self.head.data
			self.head = self.head.next
			return v
	
	def display(self):
		if(self.isEmpty()):
			print("Queue is empty")
		else:
			print("Queue contents:")
			temp = self.head
			while(temp != None):
				print(temp.data)
				temp = temp.next

def main():
	queue = LinkedQueue()

	queue.enqueue(5)
	queue.enqueue(7)
	queue.enqueue(2)
	queue.enqueue(9)
	queue.enqueue(11)

	queue.dequeue()
	queue.dequeue()

	queue.display()

main()