class queue(list):
    def __init__(self, *args):
        super().__init__(*args)
    
    def enqueue(self, item):
        self.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            del self[0]
        else:
            raise IndexError("Queue is Empty")
        
    
    def is_empty(self):
        # return len(self)==0
        return self == []
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            return self[0]
    
    def get_rear(self):
        return self[-1]

    def size(self):
        return len(self)
    
    def extend(self, iterable):
        raise NotImplementedError("extend method is not available in Queue class")
    
    def insert(self, index, item):
        raise NotImplementedError("insert method is not available in Queue class")
    
    def remove(self, item):
        raise NotImplementedError("remove method is not available in Queue class")
    
    def sort(self, *args, **kwargs):
        raise NotImplementedError("sort method is not available in Queue class")
    
    def reverse(self):
        raise NotImplementedError("reverse method is not available in Queue class")
    

q1 = queue()
q1.enqueue(11)
q1.enqueue(12)
q1.enqueue(13)
q1.enqueue(14)
q1.enqueue(15)
q1.dequeue()
print("Front :",q1.get_front())
print("Rear", q1.get_rear())
print("Size :",q1.size())