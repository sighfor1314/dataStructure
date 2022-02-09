
def ToH(n, start, buff, end):
    global count
    if n == 1:
        count+=1
        print("Disk 1 from", start, "to", end)
        return

    ToH(n - 1, start, end, buff)
    # ToH(1,A,B,C)
    count += 1
    print("Disk", n, "from", start, "to", end)
    ToH(n - 1, buff, start, end)

count=0
ToH(3, 'A', 'B', 'C')
print(count)