class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class Priority_Queue:
    def __init__(self):
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.start==None

    def push(self,item,priority):
        temp = Node(item,priority)
        # if  self.is_empty() or priority<self.start.priority:
        if not self.start or priority <self.start.priority:
            temp.next=self.start
            self.start=temp
            
        else:
            temp1=self.start
            while temp1.next and temp1.next.priority<=priority:
                temp1=temp1.next
            temp.next=temp1.next
            temp1.next=temp
        self.item_count+=1
            

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is Empty")
        else:
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data

    def size(self):
        return self.item_count
    


p=Priority_Queue()
p.push("Amit",4)
p.push("Arjun",7)
p.push("Ashima",2)
p.push("Agrah",5)
p.push("Anant",8)
p.push("Ambika",1)

while not p.is_empty():
    print(p.pop())