class Stack(list):
    def __init__(self, *args):
        super().__init__(*args)
    
    def push(self, item):
        self.append(item)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
        
    
    def is_empty(self):
        # return len(self)==0
        return self == []
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")

    def size(self):
        return len(self)
    
    def extend(self, iterable):
        raise NotImplementedError("extend method is not available in Stack class")
    
    def insert(self, index, item):
        raise NotImplementedError("insert method is not available in Stack class")
    
    def remove(self, item):
        raise NotImplementedError("remove method is not available in Stack class")
    
    def sort(self, *args, **kwargs):
        raise NotImplementedError("sort method is not available in Stack class")
    
    def reverse(self):
        raise NotImplementedError("reverse method is not available in Stack class")
    

s =  Stack()
s.push(21)
s.push(22)
s.push(23)
s.push(24)
s.pop()
print("top item is :",s.peek(),"stack size is :",s.size())
