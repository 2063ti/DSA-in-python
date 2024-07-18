class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self):
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.start==None
    
    def push(self,item):
        temp = Node(item,self.start)
        self.start=temp
        self.item_count+=1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            self.start=self.start.next
            self.item_count-=1

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            return self.start.item
    
    def size(self):
        return self.item_count
    

s=Stack()
s.push(21)
s.push(22)
s.push(23)
s.push(24)
s.pop()
print("top item is :",s.peek(),"stack size is :",s.size())