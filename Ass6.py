class Node:
    def __init__(self,item=None,next1=None,prev=None):
        self.item=item
        self.prev=prev
        self.next=next1

class Dcll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,item):
        temp=Node(item)
        if self.is_empty():
            temp.next=temp
            temp.prev=temp
        else:
            temp.next=self.start
            temp.prev=self.start.prev
            self.start.prev.next=temp
            self.start.prev=temp
        self.start=temp
            
     

    def insert_at_last(self,item):
        temp = Node(item)
        if self.is_empty():
            temp.next=temp
            temp.prev=temp
        else:
            temp.next=self.start
            temp.prev=self.start.prev
            temp.prev.next=temp
            self.start.prev=temp


    def Print_list(self):
        n= self.start
        
        while n.next is not  self.start:
            print(n.item,end=' ')
            n=n.next
            
        else:
            print(n.item,end=' ')

        
    def search(self,item):
            temp=self.start
            if temp.item==item:
                return temp
            else:
                while temp.next is not self.start:

                    temp=temp.next
                    if temp.item==item:
                        return temp
                return None
        
    def insert_after(self,after,item):
            temp1=Node(item)
            temp=self.search(after)
            if temp.next is self.start:
                    self.insert_at_last(item)
            else:  
                temp1.prev=temp
                temp1.next=temp.next
                temp.next.prev=temp1
                temp.next=temp1   

    def delete_at_first(self):
        if self.is_empty():
            print("Your list is empty :")
        else:
            self.start.next.prev=self.start.prev
            self.start.prev.next=self.start.next
            self.start=self.start.next

    def delete_at_last(self):
        if self.is_empty():
            print("Your list is empty :")
        else:
            # temp=self.start.prev
            # temp.prev.next=temp.next 
            # self.start.prev=temp.prev
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev

    def deleteitem(self,index):
        if self.is_empty():
            print("Your list is empty :")
        elif index is self.start:
            self.delete_at_first()
        elif index.prev is self.start.prev.prev :
            self.delete_at_last()
        else:
            index.next.prev=index.prev
            index.prev.next=index.next
            

dl1=Dcll()
dl1.insert_at_start(11)
dl1.insert_at_start(20)
dl1.insert_at_last(22)
dl1.insert_at_last(23)
dl1.insert_at_last(25)
dl1.insert_after(22,24)




dl1.Print_list()
print()


dl1.delete_at_first()
dl1.delete_at_last()
dl1.deleteitem(dl1.search(24))
dl1.Print_list()




