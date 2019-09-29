import random

class Element(object):
    def __init__(self,key=None,value=None,prev=None,next=None):
        self.key=key
        self.value=value
        self.prev=prev
        self.next=next

class DoublyLinkedList(object):
    def __init__(self,head=None):
        self.head=head
    def empty(self):
        if not self.head:
            return True
        else:
            return False
    def append(self,element):
        if not self.empty():
            self.head.prev=element
            element.next=self.head
            self.head=element
        else:
            self.head=element
    def find(self,key):
        if not self.empty():
            current_element=self.head
            while current_element:
                if current_element.key==key:
                    return current_element
                else:
                    current_element=current_element.next
        return None
    def remove(self,element):
        if element.prev:
            element.prev.next=element.next
        else:
            self.head=element.next
        if element.next:
            element.next.prev=element.prev

class HashTable(object):
    def __init__(self,m,p,a=None,b=None):
        self.m=m
        self.p=p
        if a:
            self.a=a
        else:
            self.a=random.uniform(1,p-1)
        if b:
            self.b=b
        else:
            self.b=random.uniform(0,p-1)
        self.chains=[DoublyLinkedList()] * m
    def hash(self,key):
        return ((self.a*key+self.b)%self.p)%self.m
    def has_key(self,key):
        chain=self.chains[self.hash(key)]
        if chain.find(key):
            return True
        else:
            return False
    def get(self,key):
        chain=self.chains[self.hash(key)]
        element_in_chain=chain.find(key)
        if element_in_chain:
            return element_in_chain.value
        else:
            return 'NA'
    def set(self,key,value):
        element=Element(key,value)
        chain=self.chains[self.hash(key)]
        if chain.find(key):
            return
        else:
            chain.append(element)
    def remove(self,key):
        chain=self.chains[self.hash(key)]
        element_in_chain=chain.find(key)
        if element_in_chain:
            chain.remove(element_in_chain)


contacts=HashTable(100,10000019,34,2)
contacts.set(2173063272,'Harshad')
contacts.set(2173067384,'Anirudh')
contacts.has_key(2173067384)
contacts.has_key(47235232)
contacts.get(2173063272)
contacts.get(2173067384)
contacts.remove(2173063272)
contacts.has_key(2173063272)
