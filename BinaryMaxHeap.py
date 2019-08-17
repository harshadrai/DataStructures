import random

class Element(object):
	def __init__(self,value=None,left=None,right=None,parent=None):
		self.value=value
		self.left=left
		self.right=right
		self.parent=parent

class BinaryMaxHeap(object):
	def __init__(self,element=None):
		self.root=element
	def get_max(self):
		return self.root.value
	def sift_up(self):
		temporary_node=self.parent
		self.parent=temporary_node.parent
		temporary_node.parent=self
		if self.value==temporary_node.left.value:
			temporary_node.left=self.left
			self.left=temporary_node
			temporary_right=self.right
			self.right=temporary_node.right
			temporary_node.right=temporary_right
		else:
			temporary_node.right=self.right
			self.right=temporary_node
			temporary_left=self.left
			self.left=temporary_node.left
			temporary_node.left=temporary_left
	def insert(self,element):
		current_element=self.root
		if not self.root:
			self.root=element
		else:
			while current_element:
				parent_element=current_element
				if random.random()<=0.5:
					current_element=current_element.left
				else:
					current_element=current_element.right
				current_element.parent=parent_element
			while current_element.parent.value < current_element.value:
				sift_up(current_element)