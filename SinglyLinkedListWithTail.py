class Element(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next


class SinglyLinkedListWithTail(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,element):
        if self.tail:
            self.tail.next=element
            element.next=None
            self.tail=element
        else:
            self.head=element
            element.next=None
            self.tail=element
    def push_front(self,element):
        if not self.tail:
            self.tail=element
        next_element=self.head
        self.head=element
        element.next=next_element
    def top_front(self):
        if self.head:
            return self.head.value
        else:
            return "Linked List is empty."
    def pop_front(self):
        if self.head:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
        else:
            return "Linked List is empty."
    def top_back(self):
        if self.tail:
            return self.tail.value
        else:
            return "Empty Linked List"
    def pop_back(self):
        if self.head:
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                prev_element=None
                next_element=self.head
                while next_element.next:
                    prev_element=next_element
                    next_element=next_element.next
                prev_element.next=None
                self.tail=prev_element
        else:
            return "Linked List is empty."
    def find(self,key):
        if self.head:
            if self.tail.value==key:
                return True
            else:
                next_element=self.head
                while next_element.next:
                    if next_element.value==key:
                        return True
                    next_element=next_element.next
                return False
        else:
            return False
    #Erase not working properly.Correct it!!!!
    def erase(self,key):
        if self.head:
            if self.head.value==key:
                if self.head.next:
                    self.head=self.head.next
                    return
                else:
                    self.head=None
                    self.tail=None
            else:
                prev_element=self.head
                next_element=self.head.next
                while next_element and next_element.value!=key:
                    prev_element=next_element
                    next_element=next_element.next
                if next_element:
                    if next_element.next:
                        prev_element.next=next_element.next
                        return
                    else:
                        prev_element.next=next_element.next
                        self.tail=prev_element
                else:
                    return str(key)+" does not exist in Linked List"
        else:
            return "Linked List is empty"
    def is_empty(self):
        if self.head:
            return False
        else:
            return True
    def add_before(self,element,key):
        if self.head:
            new_element=Element(key)
            if self.head==element:
                new_element.next=self.head
                self.head=new_element
            else:
                prev_element=self.head
                next_element=self.head.next
                while next_element and next_element!=element:
                    prev_element=next_element
                    next_element=next_element.next
                if next_element:
                    new_element.next=prev_element.next
                    prev_element.next=new_element
                else:
                    return "Given element does not exist"
        else:
            return "The Linked List is empty."
    def add_after(self,element,key):
        if self.head:
            new_element=Element(key)
            next_element=self.head
            while next_element and next_element!=element:
                next_element=next_element.next
            if next_element:
                if next_element.next:
                    new_element.next=next_element.next
                    next_element.next=new_element
                else:
                    new_element.next=next_element.next
                    next_element.next=new_element
                    self.tail=new_element
            else:
                return "Given element does not exist"
        else:
            return "The Linked List is empty."



my_list=SinglyLinkedListWithTail()
e1 = Element(5)
e2=Element(6)
e3=Element(4)
e4=Element(7)
my_list.append(e1)
my_list.append(e2)
my_list.push_front(e3)
my_list.top_front()
my_list.pop_front()
my_list.top_front()
my_list.top_back()
my_list.append(e4)
my_list.top_back()
my_list.pop_back()
my_list.top_back()
print(my_list.find(5))
print(my_list.find(9))
my_list.erase(5)
print(my_list.find(5))
my_list.erase(9)
my_list.append(Element(7))
my_list.top_back()
my_list.erase(7)
my_list.top_back()
my_list.top_front()
my_list.erase(6)
print(my_list.tail)
my_list.is_empty()
my_list.add_before(e4,7)
my_list.append(e1)
my_list.add_before(e1,4)
my_list.top_front()
my_list.add_before(e1,4.5)
print(my_list.head.next.value)
my_list.top_back()
my_list.add_after(e1,6)
my_list.top_back()
e5=my_list.head
my_list.add_after(e5,4.25)
print(my_list.head.next.value)
my_list.head=None
my_list.tail=None
my_list.is_empty()
my_list.add_after(e1,7)
my_list.push_front(e1)
print(my_list.head.next)
print(my_list.head.value)
print(my_list.tail.value)
my_list.pop_front()
print(my_list.head.value) #Should give error
print(my_list.tail.value) #Should give error
my_list.is_empty()