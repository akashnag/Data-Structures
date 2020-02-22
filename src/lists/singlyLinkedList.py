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



# Implementation of a Singly-Linked List
# Supported operations:
# - GetCount								O(1)
# - IsEmpty									O(1)
# - Append									O(1)
# - Insert Front							O(1)
# - Remove Head								O(1)
# - Remove Tail								O(n)
# - Exists									O(n)
# - Remove an arbitrary element				O(n)
# - Insert Element after a given element	O(n)
# - Display									O(n)
# - AppendList								O(m)

# Note: AppendList() can be implemented in O(1) just by setting
# two pointers but then GetCount() can not be expected to
# behave correctly. To remedy, GetCount() must be implemented in O(n).

class Node:
	def __init__(self, v):
		self.data = v
		self.next = None

	def __str__(self):
		return str(self.data)

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def getCount(self):
		return self.size
	
	def isEmpty(self):
		return(True if (self.head == None) else False)

	def append(self, v):
		temp = Node(v)
		self.size = self.size + 1
		if(self.isEmpty()):
			self.head = temp
			self.tail = temp
		else:
			self.tail.next = temp
			self.tail = temp
	
	def insertFront(self, v):
		temp = Node(v)
		self.size = self.size + 1
		if(self.isEmpty()):
			self.head = temp
			self.tail = temp
		else:
			temp.next = self.head
			self.head = temp
	
	def removeHead(self):
		if(self.isEmpty()):
			raise(Exception("Cannot remove head of empty list!"))
		else:
			self.head = self.head.next
			self.size = self.size - 1
	
	def removeTail(self):
		if(self.isEmpty()):
			raise(Exception("Cannot remove tail of empty list!"))
		elif(self.head == self.tail):
			self.head = None
			self.tail = None
			self.size = 0
		else:
			temp = self.head
			while(temp.next != self.tail):
				temp = temp.next
			temp.next = None
			self.tail = temp
			self.size = self.size - 1

	def __search(self, v):
		temp = self.head
		while(temp != None):
			if(v == temp.data):
				return temp
			temp = temp.next
		return None

	def exists(self, v):
		s = self.__search(v)
		return(True if (s != None) else False)

	def removeElement(self, v):
		if(self.isEmpty()):
			raise(Exception("Cannot remove element from an empty list"))
		elif(self.head.data == v):
			self.removeHead()
		else:
			prev = self.head
			while(prev.next.data != v):
				prev = prev.next
			prev.next = prev.next.next
			self.size = self.size - 1

	def insertAfter(self, after, v):
		a = self.search(after)
		if(a==None):
			raise(Exception("Cannot insert after non-existent element"))
		else:
			temp = Node(v)
			temp.next = a.next
			a.next = temp
			self.size = self.size + 1
	
	def display(self):
		if(self.isEmpty()):
			print("List is empty")
		else:
			print("List contents:")
			temp = self.head
			while(temp != None):
				print(str(temp))
				temp = temp.next

	def appendList(self, other):
		temp = other.head
		while(temp != None):
			self.append(temp)
			temp = temp.next

# Test function
def main():
	list1 = SinglyLinkedList()
	list2 = SinglyLinkedList()

	list1.append(4)
	list1.append(7)
	list1.append(1)
	list1.append(8)
	
	list1.removeElement(1)
	list1.insertAfter(4,6)
	
	list2.append(1)
	list2.append(5)
	list2.append(7)
	list2.append(3)
	list2.append(9)
	
	list2.removeHead()
	list2.removeTail()
	list1.appendList(list2)
	list1.insertFront(10)
	
	list1.display()
	print("# of elements = " + str(list1.getCount()))

main()
