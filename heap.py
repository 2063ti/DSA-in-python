class Heap:
    def __init__(self):
        self.heap=[]

    def create_heap(self,list1):
        for e in list1:
            self.insert(e)
        
    def insert(self,e):
        index=len(self.heap)
        parent_index=(index-1)//2
        while index>0 and self.heap[parent_index]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parent_index])
            
            else:
                self.heap[index]=self.heap[parent_index]

            index=parent_index
            parent_index=(index-1)//2

        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e

    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException
        if len(self.heap)==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()
        index=0
        left_child_index=2*index+1
        right_child_index=2*index+2

        while left_child_index<len(self.heap):
            if right_child_index<len(self.heap):
                if self.heap[left_child_index]>self.heap[right_child_index]:
                    if self.heap[left_child_index]>temp:
                        self.heap[index]=self.heap[left_child_index]
                        index=left_child_index
                    else:
                        break
                else:
                    if self.heap[right_child_index]>temp:
                        self.heap[index]=self.heap[right_child_index]
                        index=right_child_index
                    else:
                        break
            else: #no right child
                if self.heap[left_child_index]>temp:
                    self.heap[index]=self.heap[left_child_index]
                    index=left_child_index
                else:
                    break
            left_child_index=2*index+1
            right_child_index=2*index+2
        self.heap[index]=temp
        return max_value
    
    def heap_sort(self,list1):
        self.create_heap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2
    
    
class EmptyHeapException(Exception):
    def __init__(self,msg="Empty Heap"):
        self.msg=msg

    def __str__(self):
        return self.msg

list1=[34,56,12,78,43,25,10,80,60]
h1=Heap()
list1=h1.heap_sort(list1)
print(list1)
