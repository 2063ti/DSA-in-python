class Node:
    def __init__(self,item=None,next1=None,prev=None):
        self.item=item
        self.prev=prev
        self.next=next1

class Dll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,item):
        n=Node(item,self.start,None)
        self.start=n

    def insert_at_last(self,item):
        temp1=Node(item)
        if self.is_empty():
           self.start=temp1
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp1.prev=temp
            temp.next=temp1
    def search(self,item):
            temp=self.start
            if temp.item==item:
                return temp
            else:
                while temp.next is not None:

                    temp=temp.next
                    if temp.item==item:
                        return temp
                return None
        
    def insert_after(self,after,item):
            temp1=Node(item)
            temp=self.search(after)
            if temp.next is None:
                    self.insert_at_last(item)
            elif temp is not None:    
                temp1.prev=temp
                temp1.next=temp.next
                temp.next.prev=temp1
                temp.next=temp1
            


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
            if self.start is not None:
                self.start.prev=None

    def delete_at_last(self):
        if self.is_empty():
            print("Your list is empty :")
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            print(temp.item)
            # temp.prev.next=None
            temp.next=None
    def deleteitem(self,index):
        if self.is_empty():
            print("Your list is empty :")
        elif index.next is None:
            self.delete_at_last()
        elif index.prev is None:
            self.delete_at_first()
        else:
            index.next.prev=index.prev
            index.prev.next=index.next
            
        

dl1=Dll()
dl1.insert_at_start(11)
dl1.insert_at_start(20)
dl1.insert_at_last(22)
dl1.insert_at_start(5)
dl1.insert_after(5,25)
dl1.delete_at_first()
dl1.delete_at_last()
dl1.deleteitem(dl1.search(20))




dl1.Print_list()
