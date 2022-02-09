class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self,):
        self.head = None
        self.tail = None
    def printNode(self):
        ptr = self.head
        while ptr :
            print(ptr.data)
            ptr = ptr.next
            if ptr == self.tail.next:
                break
    def insertBeginning(self,new_node):
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertEndding(self,new_node):
        if self.head == None:
            self.head = new_node
        ptr=self.head
        while ptr.next:
            ptr=ptr.next
        ptr.next=new_node
        self.tail= new_node
        new_node.next=None
    def insertBetween(self,pre_node,new_node):
        # ptr= self.pre_node
        new_node.next=pre_node.next
        pre_node.next = new_node

    def deteleNode(self,value):
        ptr=self.head
        pre=ptr
        while ptr:
            if ptr.data == value:
                break
            pre=ptr
            ptr=ptr.next
        pre.next=ptr.next

    def circleLinkedlist(self):
        ptr = self.tail
        ptr.next=self.head

    def hasCycle(self):
        circle=None
        flag=True
        if self.head==None or self.head.next==None:
            flag = False
            print('False')
        slow = fast =self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                circle= slow
                count=0
                while fast and fast.next:
                    slow = slow.next
                    count+=1
                    fast = fast.next.next
                    if slow == fast:
                        break
                print('True')
                print('length = ',count)
                break
        else:
            flag = False
            print('False')
        ptr= self.head
        if flag:
            while ptr:
                if ptr == circle:
                    print(ptr.data)
                    break
                ptr=ptr.next
                circle=circle.next




# class SingleLinkedList():

sll=Linked_list()


n1=Node(1)
sll.head=n1
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
sll.insertEndding(n2)
sll.insertEndding(n3)
sll.insertEndding(n4)
sll.insertEndding(n5)
sll.insertEndding(n6)
# n6.next=n3
sll.hasCycle()


#
# sll.insertBeginning(Node(0))
# sll.insertEndding(Node(4))
# sll.insertBetween(n2,Node(2.5))
# sll.deteleNode(3)
# sll.circleLinkedlist()
# sll.printNode()
# Insert.printNode(5)





