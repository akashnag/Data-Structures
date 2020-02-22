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



# Implementation of a Binary Search Tree
# Supported Operations:
# - Insert				Omega(lg(n))
# - Delete				Omega(lg(n))
# - Exists				Omega(lg(n))
# - Display In-Order	O(n)

class BSTNode:
	def __init__(self, k, d):
		self.key = k
		self.data = d
		self.left = None
		self.right = None
		self.parent = None
	
	def __str__(self):
		if(self.data != None):
			return str(self.key) + " { " + str(self.data) + " }"
		else:
			return str(self.key)

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, key, data=None):
		node = BSTNode(key,data)
		if(self.root == None):
			self.root = node
		else:
			self.__insert(self.root, node)
	
	def __insert(self, r, node):
		if(node.key <= r.key):
			if(r.left == None):
				r.left = node
				node.parent = r
			else:
				self.__insert(r.left, node)
		else:
			if(r.right == None):
				r.right = node
				node.parent = r
			else:
				self.__insert(r.right, node)

	def displayInOrder(self):
		self.__displayInOrder(self.root)

	def __displayInOrder(self, r):
		if(r == None): return
		if(r.left != None): self.__displayInOrder(r.left)
		print(str(r))
		if(r.right != None): self.__displayInOrder(r.right)

	def exists(self, key):
		return(False if (self.__exists(self.root, key) == None) else True)

	def __exists(self, r, key):
		if(r == None): return None
		if(key == r.key):
			return r
		elif(key < r.key):
			return self.__exists(r.left, key)
		else:
			return self.__exists(r.right, key)

	def __findMin(self, r):
		if(r == None): return None		# assuming this is never reached
		if(r.left == None):
			return r
		else:
			return self.__findMin(r.left)

	def delete(self, key):
		d = self.__exists(self.root, key)
		if(d == None):
			raise(Exception("Cannot delete non-existent key"))
		elif(d.left == None and d.right == None):	# if leaf, remove it
			p = d.parent
			if(p.right == d):
				p.right = None
			else:
				p.left = None
		elif(d.left == None or d.right == None):	# has only 1 child, replace it by its child
			p = d.parent
			if(d.left != None):
				c = d.left
			else:
				c = d.right

			if(p.right == d):
				p.right = c
			else:
				p.left = c
			c.parent = p
		else:										# has 2 children, replace its contents by those of its inorder successor, and then remove the latter
			succ = self.__findMin(d.right)			# inorder successor = minimum in the right-subtree
			psucc = succ.parent
			if(succ == psucc.left):
				psucc.left = None
			else:
				psucc.right = None
			d.key = succ.key
			d.data = succ.data

# Test function
def main():
	tree = BinarySearchTree()
	
	tree.insert(5)
	tree.insert(2)
	tree.insert(9)
	tree.insert(8)
	tree.insert(11)

	tree.delete(5)
	tree.displayInOrder()

	print("9 exists: " + str(tree.exists(9)))
	print("12 exists: " + str(tree.exists(12)))

main()