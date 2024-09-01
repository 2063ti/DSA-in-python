def quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        greater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)

mylist=[53,11,72,68,41,25,18,37,44,80]
mylist=quick_sort(mylist)
print(mylist)


def merge_sort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        leftlist=list1[:mid]
        rightlist=list1[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                list1[k]=leftlist[i]
                i+=1
            else:
                list1[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            list1[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            list1[k]=rightlist[j]
            j+=1
            k+=1

mylist=[75,29,83,42,16,90,56,34,20,71,88,92,7]
merge_sort(mylist)
print(mylist)

                