class Element(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next


class Stack(object):
    def __init__(self, element=None):
        self.head=element
        self.tail=element
    def insert(self,element):
        if self.tail:
            self.tail.next=element
            element.next=None
            self.tail=element
        else:
            self.head=element
            element.next=None
            self.tail=element
    def remove(self):
        if self.head:        
            print(self.head.value)
            self.head=self.head.next
            if not self.head:
                self.tail=None
        else:
            return "Linked List is empty."


e1=Element(5)
e2=Element(6)
e3=Element(7)
my_stack=Stack(e1)
my_stack.insert(e2)
my_stack.insert(e3)
my_stack.remove()
my_stack.remove()
my_stack.remove()
my_stack.remove()
my_stack.insert(e1)
my_stack.remove()