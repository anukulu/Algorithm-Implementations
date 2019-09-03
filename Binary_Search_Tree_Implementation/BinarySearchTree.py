# All of the functions written here have been implemented using recursion (no iterations)
# Lab assignment 3 done by Anukul Parajuli / Roll no: 34 / Group: CE 3rd Year 2nd Sem

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.parent = None
		self.key = value

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def Insert(self, a):
		x = self.root
		if(x == None):
			self.root = Node(a)
			self.size += 1
		else:
			self.InsertNode(self.root, a)
	def InsertNode(self, currentNode, a):	# this is the function that inserts node into the BST
		if(currentNode.key > a):
			if(currentNode.left):
				self.InsertNode(currentNode.left, a)
			else:
				currentNode.left = Node(a)
				currentNode.left.parent = currentNode
				self.size += 1
		else:
			if(currentNode.right):
				self.InsertNode(currentNode.right, a)
			else:
				currentNode.right = Node(a)
				currentNode.right.parent = currentNode
				self.size += 1
	def SearchKey(self, searchParameter):	
		if(self.root):
			self.Search(self.root, searchParameter)
		else:
			print("The tree is empty")
	def Search(self, node, searchParameter):	# this is the function that searches for the element in the BST
		if(node):
			if(node.key == searchParameter):
				print("The value you are searching for exists in the tree")
			else:
				if(node.key > searchParameter):
					self.Search(node.left, searchParameter)
				else:
					self.Search(node.right, searchParameter)
		else:
			print("The value you are searching for does not exist in the tree")
	def SmallestKey(self):
		if(self.root):
			self.Small(self.root)
		else:
			print("The tree is empty")
	def Small(self, node):	# this is the function to find the node containing the smallest value in the BST
		if(node.left == None):
			print("The smallest key is:" + str(node.key))
		else:
			self.Small(node.left)
	def LargestKey(self):
		if(self.root):
			self.Large(self.root)
		else:
			print("The tree is empty")
	def Large(self, node):	# this is the function to find the node containing the largest value in the BST
		if(node.right == None):
			print("The largest key is:" + str(node.key))
		else:
			self.Large(node.right)
	def Preorder(self):
		if(self.root):
			self.PreorderTraversal(self.root)
		else:
			print("The tree is empty")
	def PreorderTraversal(self, node):	# this function traverses and prints the elements of BST in preorder mode (PLR)
		if(node == None):
			return
		else:
			print(node.key)
			self.PreorderTraversal(node.left)
			self.PreorderTraversal(node.right)
	def Inorder(self):
		if(self.root):
			self.InorderTraversal(self.root)
		else:
			print("The tree is empty")
	def InorderTraversal(self, node):	# this function traverses and prints the elements of BST in inorder mode (LPR)
		if(node == None):
			return
		else:
			self.InorderTraversal(node.left)
			print(node.key)
			self.InorderTraversal(node.right)
	def Postorder(self):
		if(self.root):
			self.PostorderTraversal(self.root)
		else:
			print("The tree is empty")
	def PostorderTraversal(self, node):	# this function traverses and prints the elements of BST in postorder mode (LRP)
		if(node == None):
			return
		else:
			self.PostorderTraversal(node.left)
			self.PostorderTraversal(node.right)
			print(node.key)
	def size():
		return self.size

tree = BinarySearchTree()
A= [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]
for i in A:
	tree.Insert(i)




# if(currentNode == None):   This can be implemented in C++ by using pass by reference
# 	currentNode = Node(a)
# else:
# 	if(currentNode.key < a):
# 		self.InsertNode(currentNode.right, a)
# 	else:
# 		self.InsertNode(currentNode.left, a)
