def fabonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fabonacci(n-2) + fabonacci(n-1)
for i in range(10):
    print(fabonacci(i), end = ' ')

