
class queue:
    
    def __init__(self):
        self.l1=[]

    def enqueue(self,item):
        self.l1.append(item)

    def is_empty(self):
        return self.l1 == []
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            e1 = self.l1[0]
            del self.l1[0]
            return e1
        
    def get_front(self):
        return self.l1[0]
    
    def get_rear(self):
        return self.l1[-1]
    
    def size(self):
        return len(self.l1)
    

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
