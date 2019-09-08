from math import *

class Element(object):
    def __init__(self,value=None,description=None):
        self.value=value
        self.description=description

class BinaryMaxHeap(object):
    def __init__(self,element=None):
        self.heap=[element]
        self.size=len(self.heap)
    def parent(self,position):
        return floor((position-1)/2)
    def left_child(self,position):
        return 2*position+1
    def right_child(self,position):
        return 2*position+2
    def sift_up(self,element_position):
        parent_position=self.parent(element_position)
        while element_position>0 and self.heap[element_position].value>self.heap[parent_position].value:
            self.heap[element_position],self.heap[parent_position]=self.heap[parent_position],self.heap[element_position]
            element_position=parent_position
            parent_position=self.parent(element_position)
    def sift_down(self,element_position):
        max_value_index=element_position
        l=self.left_child(element_position)
        if l<self.size and self.heap[l].value>self.heap[max_value_index].value:
            max_value_index=l
        r=self.right_child(element_position)
        if r<self.size and self.heap[r].value>self.heap[max_value_index].value:
            max_value_index=r
        if max_value_index!=element_position:
            self.heap[element_position],self.heap[max_value_index]=self.heap[max_value_index],self.heap[element_position]
            element_position=max_value_index
            self.sift_down(element_position)
    def get_max(self):
        return self.heap[0]
    def insert(self,element):
        self.heap.append(element)
        self.sift_up(self.size)
        self.size+=1
    def extract_max(self):
        if self.size>0:
            max_element=self.heap[0]
            self.heap[0]=self.heap[self.size-1]
            self.size-=1
            self.sift_down(0)
            return max_element
        else:
            return None
    def remove(self,position):
        self.heap[position].value=inf
        self.sift_up(position)
        self.extract_max()
    def change_priority(self,position,priority_value):
        previous_value=self.heap[position].value
        self.heap[position].value=priority_value
        if priority_value>previous_value:
            self.sift_up(position)
        else:
            self.sift_down(position)




e7=Element(7)
e12=Element(12)
e13=Element(13)
e11=Element(11)
e14=Element(14)
e29=Element(29)
e18=Element(18)
e18ii=Element(18)
e42=Element(42)
my_binary_heap=BinaryMaxHeap(e7)
my_binary_heap.insert(e12)
my_binary_heap.insert(e13)
my_binary_heap.insert(e11)
my_binary_heap.insert(e14)
my_binary_heap.insert(e29)
my_binary_heap.insert(e18)
my_binary_heap.insert(e18ii)
my_binary_heap.insert(e42)
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value
my_binary_heap.extract_max().value