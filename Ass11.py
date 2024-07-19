from Ass3 import *

class Stack(SLL):
    def __init__(self):
        self.l1 = SLL()
        self.item_count=0

    def is_empty(self):
        return self.l1.is_empty()
    
    def push(self,item):
        self.l1.insert_at_start(item)
        self.item_count+=1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            self.l1.delete_at_first()
            self.item_count-=1

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            return self.l1.start.item
    
    def size(self):
        return self.item_count

    
s=Stack()
s.push(21)
s.push(22)
s.push(23)
s.push(24)
print("top item is :",s.peek(),"stack size is :",s.size())
s.pop()
print("top item is :",s.peek(),"stack size is :",s.size())
    