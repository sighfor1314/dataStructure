class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
class Linked_list:
    def __init__(self,):
        self.head = None
        self.tail = None
    def printFrondNode(self):

        ptr = self.head
        while ptr:
            print(ptr.data)
            last = ptr
            ptr = ptr.next
        print('===================')
        while last :
            print(last.data)
            last = last.previous


    def insertBeginning(self,new_node):
        # new_node=Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.head.next=None
            self.head.previous=None

        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            new_node.previous =None
            self.tail = new_node



    def insertEndding(self,new_node):
        # new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.head.next = None
            self.head.previous = None

        ptr=self.head
        while ptr.next:
            ptr=ptr.next
        ptr.next=new_node
        new_node.previous = ptr
        new_node.next=None
        self.tail=new_node


    def insertBetween(self,prev_node,new_node):

        new_node.next=prev_node.next
        prev_node.next = new_node

        new_node.previous = prev_node
        if new_node.next:
            new_node.next.previous = new_node
    def printEnd(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous

    def linkCount(self):
        count=0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            count +=1
        print('count = ',count)

    def deleteNode(self,new_data):
        ptr = self.head
        pre = ptr
        while ptr:
            if ptr.data == new_data:
                break
            pre = ptr
            ptr = ptr.next

        if ptr == self.head: #data在head
            self.head.next.previous = None
            self.head = self.head.next
        elif ptr == self.tail: #data in tail
            self.tail.previous.next = None
            self.tail = self.tail.previous
        else:
            pre.next = ptr.next
            ptr.next.previous = pre

    def reciprocalKnode(self, k):
        ptr = self.tail
        for i in range(k):
            ptr = ptr.previous
            print(ptr.data)
            break


# class SingleLinkedList():

dll=Linked_list()

# n0.next=n1
# n1.previous=n0
# n1.next=n3
# n3.previous=n1
# dll.head=n0
#
n0=Node(0)
n1=Node(1)
n2=Node(2)
n3=Node(3)
dll.insertBeginning(n0)
dll.insertEndding(n1)
dll.insertEndding(n3)


dll.insertBetween(n1,Node(2))
# dll.printFrondNode()
dll.linkCount()

# dll.deleteNode(3)
dll.printFrondNode()
print('----------------------------------')
# dll.printEnd()

dll.reciprocalKnode(2)









# program to demonstrate all
# insertion methods

# # A linked list node
# class Node:
#
#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
#
# # Class to create a Doubly Linked List
# class DoublyLinkedList:
#
#     # Constructor for empty Doubly Linked List
#     def __init__(self):
#         self.head = None
#
#     # Given a reference to the head of a list and an
#     # integer, inserts a new node on the front of list
#     def push(self, new_data):
#
#         # 1. Allocates node
#         # 2. Put the data in it
#         new_node = Node(new_data)
#
#         # 3. Make next of new node as head and
#         # previous as None (already None)
#         new_node.next = self.head
#
#         # 4. change prev of head node to new_node
#         if self.head is not None:
#             self.head.prev = new_node
#
#         # 5. move the head to point to the new node
#         self.head = new_node
#
#     # Given a node as prev_node, insert a new node after
#     # the given node
#     def insertAfter(self, prev_node, new_data):
#
#         # 1. Check if the given prev_node is None
#         if prev_node is None:
#             print("the given previous node cannot be NULL")
#             return
#
#         # 2. allocate new node
#         # 3. put in the data
#         new_node = Node(new_data)
#
#         # 4. Make net of new node as next of prev node
#         new_node.next = prev_node.next
#
#         # 5. Make prev_node as previous of new_node
#         prev_node.next = new_node
#
#         # 6. Make prev_node ass previous of new_node
#         new_node.prev = prev_node
#
#         # 7. Change previous of new_nodes's next node
#         if new_node.next:
#             new_node.next.prev = new_node
#
#     # Given a reference to the head of DLL and integer,
#     # appends a new node at the end
#     def append(self, new_data):
#
#         # 1. Allocates node
#         # 2. Put in the data
#         new_node = Node(new_data)
#
#         # 3. This new node is going to be the last node,
#         # so make next of it as None
#         # (It already is initialized as None)
#
#         # 4. If the Linked List is empty, then make the
#         # new node as head
#         if self.head is None:
#             self.head = new_node
#             return
#
#         # 5. Else traverse till the last node
#         last = self.head
#         while last.next:
#             last = last.next
#
#         # 6. Change the next of last node
#         last.next = new_node
#
#         # 7. Make last node as previous of new node
#         new_node.prev = last
#
#         return
#
#     # This function prints contents of linked list
#     # starting from the given node
#     def printList(self, node):
#
#         print("\nTraversal in forward direction")
#         while node:
#             print(" {}".format(node.data))
#             last = node
#             node = node.next
#
#         print("\nTraversal in reverse direction")
#         while last:
#             print(" {}".format(last.data))
#             last = last.prev
#
#
# # Driver program to test above functions
#
#
# # Start with empty list
# llist = DoublyLinkedList()
#
# # Insert 6. So the list becomes 6->None
# llist.append(6)
#
# # Insert 7 at the beginning.
# # So linked list becomes 7->6->None
# llist.push(7)
#
# # Insert 1 at the beginning.
# # So linked list becomes 1->7->6->None
# llist.push(1)
#
# # Insert 4 at the end.
# # So linked list becomes 1->7->6->4->None
# llist.append(4)
#
# # Insert 8, after 7.
# # So linked list becomes 1->7->8->6->4->None
# llist.insertAfter(llist.head.next, 8)
#
# print("Created DLL is: ")
# llist.printList(llist.head)
#
# # This code is contributed by Nikhil Kumar Singh(nickzuck_007)