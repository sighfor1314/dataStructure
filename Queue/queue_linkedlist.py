'''
Queue first in first out FIFO
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self,):
        self.head = None
        self.tail = None
    def printNode(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next


    def insertNode(self,new_node):
        if self.head == None:
            self.head = new_node
            self.head.next = None
        else:
            ptr=self.head
            while ptr.next:
                ptr=ptr.next
            ptr.next=new_node
            self.tail = new_node

    def deteleNode(self):

        self.head= self.head.next

    def linkCount(self):
        count=0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            count +=1
        print('count = ',count)

qu=Queue()
qu.insertNode(Node(0))
qu.insertNode(Node(1))
qu.insertNode(Node(2))
qu.printNode()
print('------------------------------------------------')
qu.deteleNode()
qu.printNode()
qu.linkCount()