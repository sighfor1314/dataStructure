# # class TreeNode:
# #     def __init__(self, value):
# #         self.left = None
# #         self.right = None
# #         self.data = value
# #
# # class Tree:
# #     def __init__(self):
# #         self.root = None
# #
# #     def insert1(self, value):
# #        # 判斷tree是否為空
# #         if self.root == None:
# #             self.root = TreeNode(value)
# #         else:
# #             self.insert(value, self.root)
# #     def insert(self,value,node=None):
# #
# #         # if node == None:
# #         #     self.root = TreeNode(value)
# #         #     # node = self.root
# #         # else:
# #             if node.data > value:
# #                 if node.left :
# #                     self.insert(value,node.left)
# #                 else:
# #                    node.left = TreeNode(value)
# #
# #             else:
# #                 if node.right :
# #                     self.insert(value,node.right)
# #                 else:
# #                     node.right = TreeNode(value)
# #
#
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.right = None
#         self.left = None
#
# class Tree:
#     def __init__(self):
#         self.root = None
#     # def insert(self,value):
#     #     # 判斷tree是否為空
#     #     if self.root == None:
#     #         self.root = Node(value)
#     #     else:
#     #         self._insert(value,self.root)
#     #
#     # def _insert(self,value,root=None):
#     #
#     #         if value < root.value:
#     #             if root.left:
#     #                 self._insert(value, root.left)
#     #             else:
#     #                 root.left= Node(value)
#     #         else :
#     #             if root.right:
#     #                 self._insert(value, root.right)
#     #             else:
#     #                 root.right = Node(value)
#     #
#     # def printInorder(self, node):
#     #     if(node!=None):
#     #         self.printInorder(node.left)
#     #         print(node.value)
#     #         self.printInorder(node.right)
#
#     def loopInsert(self,label):
#         # Create a new Node
#         new_node = Node(label)
#         # If Tree is empty
#         if not self.root:
#             self.root = new_node
#         else:
#             # If Tree is not empty
#             curr_node = self.root
#             # While we don't get to a leaf
#             while curr_node is not None:
#                 # We keep reference of the parent node
#                 parent_node = curr_node
#                 # If node label is less than current node
#                 if new_node.getLabel() < curr_node.getLabel():
#                     # We go left
#                     curr_node = curr_node.getLeft()
#                 else:
#                     # Else we go right
#                     curr_node = curr_node.getRight()
#             # We insert the new node in a leaf
#             if new_node.getLabel() < parent_node.getLabel():
#                 parent_node.setLeft(new_node)
#             else:
#                 parent_node.setRight(new_node)
#             # Set parent to the new node
#             new_node.setParent(parent_node)
#

testTree = Tree()
# testTree.insert(300,testTree.root)
# testTree.insert(200,testTree.root)
# testTree.insert(400,testTree.root)
# testTree.printInorder(testTree.root)
# testTree.find()
# print('============================')
# testTree.insert(200,testTree.root)
# testTree.printInorder(testTree.root)
# print('============================')
testTree.insert(300)
testTree.insert(100)
testTree.insert(30)
testTree.printInorder(testTree.root)
