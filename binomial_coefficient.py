'''
            n!
c(n,m) = --------
        m! (n-m)!
c(n,m) = c (n-1,m)+ c(n-1,m-1)

'''
'''
c(n,m) = c(5,2) 從五個元素中取2個的組合
'''

def recurtion(n,m):
    print('n = ', n, 'm = ', m)
    if m==0 or n==m:
        return 1
    else:
        return recurtion(n-1,m-1)+recurtion(n-1,m)


a=recurtion(5,2)
print(a)


