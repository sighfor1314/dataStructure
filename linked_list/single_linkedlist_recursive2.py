class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def printNode(self,node):
        # ptr = head
        if node:
            print(node.data)
            self.printNode(node.next)
    def insertBeginning(self,new_node):
        if self.head == None:
            self.head = new_node
            self.head.next = None
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
        self.tail = new_node


    def insertBetween(self,pre_node,new_node):

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
        del ptr
    def linkCount(self):
        count=0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            count +=1
        print('count = ',count)

    def reverse(self):
        pre = None
        ptr = self.head
        current = ptr.next

        while ptr:
            ptr.next = pre
            pre = ptr
            ptr = current
            if current:
                current = current.next
        self.head=pre

    def printEnd(self):
        lst=[]
        ptr=self.head
        while ptr:
            lst.append(ptr.data)
            ptr=ptr.next
        for i in range(len(lst)):
            i=lst.pop()
            print(i)

    def deleteO1(self,node):
        if node== self.head:
            self.head = node.next
            node.next=None
        else:
            ptr = node
            ptr.data = ptr.next.data
            ptr.next= ptr.next.next
        del node

    def sameNode(self,node_1,node2):
        count1=0
        count2=0

        ptr1 = node_1
        ptr2 = node2
        while ptr1:
            count1+=1
            ptr1 = ptr1.next
        while ptr2:
            count2+=1
            ptr2 = ptr2.next
        length=abs(count1-count2)
        ptr1 = node_1
        ptr2 = node2
        if count1>count2:
            for i in range(length):
                ptr1=ptr1.next
            while ptr1:
                if ptr1==ptr2:
                    print(ptr1.data)
        else:
            for i in range(length):
                ptr2=ptr2.next
            while ptr1:
                if ptr1==ptr2:
                    print(ptr1.data)
                    break

    def reversee(self,head):
        if not head or not head.next:
            return head

        ptr = head.next
        head.next = None
        new_node = self.reversee(ptr)
        ptr.next = head
        return new_node


    # def mergeList(self,arr):
    #     ptr=self.head
    #     while ptr:
    #         if


sll=Linked_list()

arr=[3,5,6,7,8]
n1=Node(1)
sll.head=n1
n2=Node(2)
sll.head.next=n2
n3=Node(3)
n2.next=n3
n0=Node(0)
n7=Node(7)
n8=Node(8)


# sll.insertBeginning(n0)
sll.insertEndding(Node(4))
sll.insertEndding(Node(7))
# sll.insertBetween(n2,Node(2.5))
# sll.deteleNode(2.5)
# sll.printNode()
# sll.linkCount()

# print('-----------------------')
# # sll.reverse()
# sll.printNode()
# print('----------------------------------')
# sll.printEnd()
# #
# sll.deleteO1(n0)
# print('----------------------------------')
# sll.printNode()
sll.reversee(sll.head)
sll.printNode(sll.head)




