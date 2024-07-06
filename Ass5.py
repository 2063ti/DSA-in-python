
class Node:
    def __init__(self,item=None,next1=None):
        self.item=item
        self.next=next1



class Cll:
    def __init__(self,tail=None):
        self.tail=tail

    def is_empty(self):
        return self.tail==None
    
    def Print_list(self):

        n= self.tail.next
        while n.next is not self.tail.next:
            print(n.item,end=' ')
            n=n.next
        else:
            print(n.item,end=' ')

    def insert_at_start(self,item):
        if self.is_empty():
            n=Node(item,self.tail)
            self.tail=n
            self.tail.next=n
        else :
            n= Node(item,self.tail.next)
            self.tail.next=n
        
    def insert_at_last(self,item):
        if self.is_empty():
            n=Node(item,self.tail)
            self.tail=n
            self.tail.next=n
        else :
            n=Node(item,self.tail.next)
            self.tail.next=n
            self.tail=n

    def insert_after(self,temp,item):
        if self.tail.next == temp.next:
            self.insert_at_last(item)
        else:
            n= Node(item,temp.next)
            temp.next=n

    def search(self,item):
            n= self.tail.next
            while n is not self.tail:
                if n.item==item:
                    return n
                n=n.next
            if n.item==item:
                    return n
            else:
                return None
            
    def delete_at_first(self):
        if self.is_empty():
            print("Your list is empty :")
        else:
            self.tail.next=self.tail.next.next

    def delete_at_last(self):
        if self.is_empty():
            print("Your list is empty :")
        elif self.tail.next==self.tail:
            self.tail=None
        else:
            temp=self.tail
            while temp.next.next is not self.tail:
                temp=temp.next
            else :
                temp.next.next=self.tail.next
                self.tail=temp.next

    def delete_item(self,data):
        if self.is_empty():
            print("Your list is empty :")
        
        else:
            temp=self.tail
            if  temp.item==data :
                self.delete_at_last()
            else:
                while temp.next is not self.tail:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

            


            


cl1 = Cll()
cl1.insert_at_start(10)
cl1.insert_at_last(11)
cl1.insert_at_start(12)
cl1.insert_after(cl1.search(11),30)
cl1.insert_after(cl1.search(10),50)
cl1.Print_list()
print()
cl1.delete_at_first()
print()
cl1.Print_list()
print()
cl1.delete_at_last()
cl1.Print_list()
print()
cl1.delete_item(11)
cl1.Print_list()

