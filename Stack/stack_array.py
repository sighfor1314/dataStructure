'''
Stack first in last out FILO
'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items ==[]:
            return print('this is empty')
        else :
            return print('裡面還有值')
    def pushData(self, item): # 從list index = 0 處開始加入item
        self.items.append(item)

    def popData(self):       # 從list index = -1 處del item
        return self.items.pop()

    def printdata(self):
        for item in self.items:
            print(item)

sta = Stack()
sta.pushData(0)
sta.pushData(1)
sta.pushData(2)
sta.printdata()
print('--------------------------')
sta.popData()
sta.printdata()

