'''
Queue first in first out FIFO
'''

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items ==[]:
            return print('this is empty')
        else :
            return print('裡面還有值')
    def enqueue(self, item): # 從list index = 0 處開始加入item
        self.items.insert(0,item)

    def dequeue(self):       # 從list index = -1 處del item
        return self.items.pop()

    def printdata(self):
        for item in self.items:
            print(item)

qu = Queue()
qu.enqueue(0)
qu.enqueue(1)
qu.enqueue(2)
qu.printdata()
print('--------------------------')
qu.dequeue()
qu.printdata()

