class stack:
    def __init__(self):
        self.l1=[]

    def push(self,item):
        self.l1.append(item)
        

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            return self.items.pop()
            # del self.l1[-1]
            

    def is_empty(self):
        # return len(self.items)==0
        return self.l1 == []

    def peek(self):
        if not self.is_empty():
            return self.l1[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return len(self.l1)

   
    


s = stack()

s.push(23)
s.push(24)
s.push(25)
s.push(26)
print("popped item is :",s.pop())
print("Top element is",s.peek())
