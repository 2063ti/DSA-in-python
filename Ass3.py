# Singly Link list
class Node :
    def __init__(self,item=None,next1=None):
        self.item=item
        self.next=next1

class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,item):
        n=Node(item,self.start)
        self.start=n

    def insert_at_last(self,item):
        temp=Node(item)
        if self.is_empty():
            self.start=temp
        else :
            temp1=self.start
            while temp1.next is not None:
                temp1=temp1.next
            temp1.next=temp
    def insert_after(self,index,item):

        if index is not None:
            n=Node(item,index.next)
            index.next=n

    def search(self,data):
        n=self.start
        while n is not None:
            if n.item == data :
                return n
            n=n.next
        return None
    def Print_list(self):
        n= self.start
        while n is not None:
            print(n.item,end=' ')
            n=n.next
    def delete_at_first(self):
        if self.is_empty():
            print("Your list is empty :")
        else:
            self.start=self.start.next

    def delete_at_last(self):
        if self.is_empty():
            print("Your list is empty :")
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            else :
                temp.next=None
    def delete_item(self,data):
        if self.is_empty():
            print("Your list is empty :")
        
        else:
            temp=self.start
            if  temp.item==data :
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
            

            
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data 
mylist = SLL()
# mylist.delete_at_first()
mylist.delete_at_last()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),30)
mylist.insert_after(mylist.search(30),40)
mylist.insert_at_start(50)
mylist.insert_at_last(60)
mylist.Print_list()
mylist.delete_at_first()
mylist.delete_at_last()
mylist.delete_item(30)

print()

for x in mylist:
    print(x,end=' ')

print()