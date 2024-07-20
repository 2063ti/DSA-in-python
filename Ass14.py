class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    
    def enqueue(self,item):
        temp= Node(item)
        if self.is_empty():
            self.front=temp
            self.rear=temp
            self.item_count+=1
        else:
            self.rear.next=temp
            self.rear=temp
            self.item_count+=1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            self.front = self.front.next
            self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count

 
q1 = Queue()
q1.enqueue(11)
q1.enqueue(12)
q1.enqueue(13)
q1.enqueue(14)
q1.enqueue(15)
q1.dequeue()
print("Front :",q1.get_front())
print("Rear", q1.get_rear())
print("Size :",q1.size())