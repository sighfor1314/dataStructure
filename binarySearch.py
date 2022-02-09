import random
length=random.randint(100,200)
lst=[]
for i in range(length):
    lst.append(random.randint(0,10000))
lst_sorted=sorted(lst)

print (lst_sorted)
low=0
upper=len(lst_sorted)-1
key=input("input key : ")
while low < upper :

    mid = (low + upper) // 2
    # print ('low=',low,'  upp=',upper,'  mid=',mid)

    if int(key) > lst_sorted[mid] :
        low = mid+1
    elif int(key) < lst_sorted[mid] :
        upper = mid -1
    else:

        print('key %s on %d ' %( key,mid))
        break;

else:
    print ('%s nofound' %key)