class Node:
    def __init__(self,item=None,next=None,prev=None):
        self.prev=prev
        self.next=next
        self.item=item

class deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    
    def insert_front(self,item):
        temp = Node(item)
        if self.is_empty():
            self.rear=temp
        else:
            self.front.prev=temp
            temp.next=self.front
        self.front=temp
        self.item_count+=1

    def insert_rear(self,item):
        temp = Node(item)
        if self.is_empty():
            self.front=temp
        else:
            self.rear.next=temp
            temp.prev=self.rear
        self.rear=temp
        self.item_count+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        elif self.front == self.rear:
            self.rear=None
            self.front=None
        else:
            self.front=self.front.next
            if self.front is not None:
                self.front.prev=None
        self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        elif self.front == self.rear:
            self.rear=None
            self.front=None
        else:
            self.rear=self.rear.prev
            if self.rear is not None:
                self.front.prev=None
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        else:
            return self.rear.item

    def size(self):
        return self.item_count
    

d = deque()
d.insert_front(11)
d.insert_front(12)
d.insert_rear(13)
d.delete_front()
d.delete_rear()
print("Size is :",d.size())
print("Front is :",d.get_front())
print("Rear is :",d.get_rear())