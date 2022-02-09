class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


count = 0
class Tree:
    def __init__(self):
        self.root =None
    def insert2(self,value,root=None):
        if root==None:
            root=self.root

        if self.root:
            if root.value > value:
                if root.left:
                    self._insert(value, root.left)
                else:
                    root.left = Node(value)
            else:
                if root.right:
                    self._insert(value, root.right)
                else:
                    root.right = Node(value)
        else:
            self.root = Node(value)
    def insert(self,value):
        if self.root:
            self._insert(value,self.root)
        else:
            self.root = Node(value)
    def _insert(self,value,root):
        if root.value > value:
            if root.left:
                self._insert(value,root.left)
            else:
                root.left = Node(value)
        else:
            if root.right:
                self._insert(value, root.right)
            else:
                root.right = Node(value)

    def printInorder(self, node):

        if(node!=None):
                self.printInorder(node.left)
                print(node.value)
                self.printInorder(node.right)

    def inOrder(self):
        node = self.root
        if node:
            self._inOrder(node)
        else:
            print('Root not Exist')
    def _inOrder(self,node):
        # node = self.root
        if node:
            if node.left:
                self._inOrder(node.left)
            print(node.value)
            if node.right:
                self._inOrder(node.right)

        else:
            print('Root not Exist')
    def inOrder2(self,k,node=None):

        if node ==None:
            node=self.root
        # if node.left == None and node.right == None:
            # print('leaf= ', node.value)
            #
            # return count + 1
        if node:
            # if k == 0:
            #     print('k= ', node.value)
            if node.left:
                self.inOrder2(k,node.left)
            print(node.value)
            k-=1
            if k==0:
                print('k=',node.value)

            if node.right:
                self.inOrder2(k,node.right)

        else:
            print('Root not Exist')

        # print('count= ',count)
    def preOrder2(self,node=None):

        if node ==None:
            node=self.root
        if node:
            if node:
                print(node.value)
                if node.left:
                    self.preOrder2(node.left)
                if node.right:
                    self.preOrder2(node.right)
        else:
            print('Root not Exist')
    def postOrder2(self,node=None):

        if node ==None:
            node=self.root
        if node:
            if node:

                if node.left:
                    self.postOrder2(node.left)
                if node.right:
                    self.postOrder2(node.right)
                print(node.value)
        else:
            print('Root not Exist')
    def search(self,value,root=None):
        if root == None:
            root = self.root

        if self.root:
            if root.value > value:
                if root.left:
                    self.search(value, root.left)
                else:
                    print('不存在')
            elif root.value < value:
                if root.right:
                    self.search(value, root.right)
                else:
                    print('不存在')
            else:
                print('找到')
        else:
            self.root = Node(value)

    def getLeafCount(self,node):
        if node is None:
            return 0
        if (node.left is None and node.right is None):
            return 1
        else:
            return self.getLeafCount(node.left) + self.getLeafCount(node.right)

    # def delete(self,value,root=None):
    #     if root == None:
    #         root = self.root
    #     if self.root == None:
    #         return None
    #     if value > root.value:
    #         root.right = self.delete(value,root.right)
    #     elif value < root.value:
    #         root.left = self.delete(value,root.left)
    #     else:
    #         if root.left ==None:
    #             return root.right
    #         if root.right ==None:
    #             return root.left
    #
    #         min_node= self.getMin(root.right)
    #         root.value = min_node.value
    #         root.right= self.delete(min_node.value,root.right)
    #
    #     return root
    # def getMin(self,root):
    #     while root.left:
    #         root=root.left
    #     return root

    def delete(self,value,root=None):
        if root == None:
            root = self.root
        if self.root == None:
            return None
        if root.value < value:
            root.right = self.delete(value,root.right)
        elif root.value > value:
            root.left = self.delete(value, root.left)
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            minNode = self.getMin(root.right)
            root.value= minNode.value
            root.right =self.delete(minNode.value, root.right)
        return root
    def delete1(self,value,root=None):
        if root == None:
            root = self.root
        if self.root == None:
            return None
        if root.value < value:
            root.right = self.delete1(value,root.right)
        elif root.value > value:
            root.left = self.delete1(value, root.left)
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            minNode = self.getMax(root.left)
            root.value= minNode.value
            root.left = self.delete1(minNode.value, root.left)
        return root

    def getMin(self,root):
        while root.left:
            root=root.left
        return root

    def getMax(self, root):
        while root.right:
            root = root.right
        return root

    def maxValue(self):
        root = self.root
        while root.right:
            root = root.right
        return root.value
    def minValue(self):
        root = self.root
        while root.left:
            root = root.left
        return root.value
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return


    # 我們要在每一次遞迴呼叫時傳入cur_height，如果沒有像parameter
    # 樣傳入或儲存成global variable會造成 無法儲存cur_height
    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height #0
        # 找一個最高的子樹
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right,cur_height+1)

        return max(left_height, right_height)

    def low(self):
        if self.root != None:
            return self._low(self.root,0)
        else:
            return


    # 我們要在每一次遞迴呼叫時傳入cur_height，如果沒有像parameter
    # 樣傳入或儲存成global variable會造成 無法儲存cur_height
    def _low(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height #0
        # 找一個最高的子樹
        left_height = self._low(cur_node.left,cur_height+1)
        right_height = self._low(cur_node.right,cur_height+1)

        return min(left_height, right_height)



    def isBalance(self,root):
        left_height = self._height(root.left, root + 1)
        right_height = self._height(root.right, root + 1)

        if abs(left_height -right_height) >1:
            return  False
        else:
            return True

    def getDeepth(self, Root):
        if Root is None:
            return 0
        nright = self.getDeepth(Root.right)
        nleft = self.getDeepth(Root.left)

        return max(nright, nleft) + 1


    def IsBalance_solution(self, pRoot):
        if pRoot is None:
            return True
        right = self.getDeepth(pRoot.right)
        left = self.getDeepth(pRoot.left)
        if abs(right - left) > 1:
            return False
        return self.IsBalance_solution(pRoot.right) and self.IsBalance_solution(pRoot.left)
    # def _isBalance(self,root):
    #     left_height = self._height(root.left, root + 1)
    #     right_height = self._height(root.right, root + 1)
    #
    #     if abs(left_height -right_height) >1:
    #         return  False
    #     else:
   #         return True
    def level_order(self,root):
        if not root:  return []
        queue = [root]
        while queue:
            levelQueue = []
            for i in range(len(queue)):
                node = queue.pop(0)
                levelQueue.append(node.value)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            print(levelQueue)
        # print(res)

        # if root == None:
        #     return
        # myQueue = []
        # node = root
        # myQueue.append(node)
        # while myQueue:
        #     print(node.value)
        #     node = myQueue.pop(0)
        #
        # if node.left != None:
        #     myQueue.append(node.left)
        # if node.right != None:
        #     myQueue.append(node.right)
        # #
        #     queue = [root]
        #     while len(queue) != 0:
        #         curr = queue[0]
        #         queue = queue[1:]
        #         print(str(curr.value + " ", end="")
        #         if curr.left is not None:
        #             queue.append(curr.left)
        #         if curr.right is not None:
        #             queue.append(curr.right)
        # traversed = []
        # traversed.append(root)
        # if root is None:
        #     return traversed
        # while traversed != []:
        #     print(traversed[0].value)
        #     x = traversed.pop(0)
        #     if x.left:
        #         traversed.append(x.left)
        #     if x.right:
        #         traversed.append(x.right)

    def inOrder3(self, node,k):
        if node == None:
            node = self.root
        if node:
            if node.left:
                self.inOrder3(node.left,k)
            self.count.append(node.value)

            if node.right:
                self.inOrder3(node.right,k)

        else:
            print('Root not Exist')

    def kth(self,root,k):
        self.count=[]
        self.inOrder3(root,k)
        print(self.count[k-1])

    def nth(self,root,k):
        self.c=0
        self.inOrder4(root,k)

    def inOrder4(self, node,k):
        if node == None:
            node = self.root
        if node:
            if node.left:
                self.inOrder4(node.left,k)
            self.c+=1
            if self.c == k:
                print(node.value)

            if node.right:
                self.inOrder4(node.right,k)

        else:
            print('Root not Exist')
testTree = Tree()
testTree.insert2(30)
testTree.insert2(40)
testTree.insert2(10)
testTree.insert2(5)
# testTree.insert2(60)
# testTree.insert2(4)
testTree.insert2(7)
testTree.insert2(50)
testTree.insert2(35)
testTree.insert2(25)
# testTree.insert2(26)
# testTree.insert2(27)
# print(testTree.getLeafCount(testTree.root))
# testTree.insert2(3)
# testTree.insert2(70)
# print(testTree.height())
# print(testTree.height())
# print(testTree.low())
# testTree.inOrder()
# # print(testTree.isBalance(testTree.root))
# print(testTree.getDeepth(testTree.root))
# print(testTree.IsBalance_solution(testTree.root))
# testTree.postOrder2()
# testTree.search(20)
# testTree.search(25)
# testTree.search(15)
# testTree.search(17)
# testTree.search(18)
# testTree.search(13)
# testTree.search(9)
# testTree.search(33)
# testTree.search(22)
# testTree.search(23)
# testTree.delete1(20)
# testTree.inOrder2(3)
# print(testTree.maxValue())
# print(testTree.minValue())
# testTree.printInorder(testTree.root)
# testTree.level_orde)
# testTree.kth(testTree.root,3)
# testTree.inOrder3(testTree.ro
# ot,3)
testTree.nth(testTree.root,4)