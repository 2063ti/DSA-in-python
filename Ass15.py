class deque:

    def __init__(self):
        self.l1 = []

    def insert_front(self,item):
        self.l1.insert(0,item)

    def insert_rear(self,item):
        self.l1.append(item)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        else:
            del self.l1[0]

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        else:
            del self.l1[-1]

    def get_front(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        else:
            return self.l1[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("DeQue is Empty")
        else:
            return self.l1[-1]

    def is_empty(self):
        return self.l1 == []

    def size(self):
        return len(self.l1)
    

d = deque()
d.insert_front(11)
d.insert_front(12)
d.insert_rear(13)
d.delete_front()
d.delete_rear()
print("Size is :",d.size())
print("Front is :",d.get_front())
print("Rear is :",d.get_rear())