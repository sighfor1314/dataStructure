def create_tree(BT,data):
    for i in range(len(data)):
        level =0
        if i ==0:
            BT[level] = data[i]
        else:
            while BT[level] :  # while BT[level] != None :
                if BT[level] < data[i]:
                    level = 2*level +2
                else:
                    level = 2 * level + 1
            BT[level] =data[i]
            print(i, BT)

data=[5,9,13,4,1,25]
BT = [None]*16
create_tree(BT,data)
for i in range(len(BT)):
    print(i,BT[i])