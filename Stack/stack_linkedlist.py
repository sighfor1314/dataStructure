'''
Stack first in last out FILO
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
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
        ptr = self.head
        while ptr.next != self.tail:
            ptr = ptr.next

        ptr.next=None
        self.tail = ptr


    def linkCount(self):
        count=0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            count +=1
        print('count = ',count)

sta=Stack()
sta.insertNode(Node(0))
sta.insertNode(Node(1))
sta.insertNode(Node(2))
sta.printNode()
print('------------------------------------------------')
sta.deteleNode()
sta.printNode()
sta.linkCount()
print('-------------------------------')
sta.deteleNode()
sta.printNode()
sta.linkCount()