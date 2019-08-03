class Element(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next


class Queue(object):
    def __init__(self, element=None):
        self.head=element
        self.tail=element
    def enqueue(self,element):
        if self.tail:
            self.tail.next=element
            element.next=None
            self.tail=element
        else:
            self.head=element
            element.next=None
            self.tail=element
    def dequeue(self):
        if self.head:        
            exiting_element=self.head
            print(exiting_element.value)
            self.head=self.head.next
            if not self.head:
                self.tail=None
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
my_queue=Queue(e1)
my_queue.enqueue(e2)
my_queue.enqueue(e3)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.enqueue(e1)
my_queue.dequeue()
my_queue.is_empty()
