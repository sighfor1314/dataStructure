def mergeSort(lst1,lst2):
    result=[]
    while len(lst1) and len(lst2):
        if lst1[0]<lst2[0]:
            result.append(lst1.pop(0))
        else:
            result.append(lst2.pop(0))

    result= result+lst1 if len(lst1) else result+lst2
    print(result)

lst1=[1,4,5,7,9,22]
lst2=[0,2,3,5,8,11,66,78]
print(lst1+lst2)
mergeSort(lst1,lst2)