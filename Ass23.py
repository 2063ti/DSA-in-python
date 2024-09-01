#BUbble sort
class Sort:
    def __init__(self,l1=[]):
        self.l1=l1

    def bubble_sort(self):
        for i in range(len(self.l1)-1):
            # print("round:",i,len(self.l1))
            # print("list:",self.l1)
            for j in range(0,len(self.l1)-1-i):
                # print(j)
                if self.l1[j] > self.l1[j+1]:
                    temp = self.l1[j]
                    self.l1[j]=self.l1[j+1]
                    self.l1[j+1]=temp
        return self.l1
    
    def modified_bubble_sort(self):
        pass
    def selection_sort(self):
       
        for i in range(len(self.l1)-1):
            m=i
            # print("round:",i,len(self.l1))
            
            for j in range(i+1,len(self.l1)):
                # print(i,j)
                if self.l1[m]>self.l1[j]:
                    m=j
            if m!=i:
                temp=self.l1[i]
                self.l1[i]=self.l1[m]
                self.l1[m]=temp

            # print("list:",self.l1)
        return self.l1
    
    def insertion_sort(self):
        for i in range(10-1):
            # print("round:",i,len(self.l1))
            # print(self.l1)
            # if self.l1[i]>self.l1[i+1]:
            #     temp=self.l1[i+1]
            #     self.l1[i+1]=self.l1[i]
            #     self.l1[i]=temp
            for j in range(i+1,0,-1):
                # print(i,j)
                if self.l1[j-1]>self.l1[j]:
                    temp=self.l1[j]
                    self.l1[j]=self.l1[j-1]
                    self.l1[j-1]=temp

            # print(self.l1)
        return self.l1

            




list_of_elements=[24,58,11,67,92,43]
list_of_elements1=[38,90,47,69,52,88,71,18,20]
list_of_elements2=[50,20,37,91,64,18,43,59,72,81]

l1=Sort(list_of_elements2)
print("Sorted list of elements are :",l1.insertion_sort())
# print("Sorted list of elements are :",l1.selection_sort())
# print("Sorted list of elements are :",l1.bubble_sort())
