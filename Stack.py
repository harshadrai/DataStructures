class Element(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next


class Stack(object):
    def __init__(self, element=None):
        self.head=element
    def push(self,element):
        next_element=self.head
        self.head=element
        element.next=next_element
    def pop(self):
        if self.head:
            exiting_element=self.head       
            print(exiting_element.value)
            self.head=self.head.next
            return exiting_element
        else:
            return "Linked List is empty."
    def is_empty(self):
        if self.head:
            return False
        else:
            return True

e1=Element(5)
e2=Element(6)
e3=Element(7)
my_stack=Stack(e1)
my_stack.push(e2)
my_stack.push(e3)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.push(e1)
my_stack.pop()
my_stack.is_empty()