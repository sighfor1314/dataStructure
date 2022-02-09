# Definition for singly-linked list.
#leetcode複製貼上 測資產生待測試
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        output = ListNode(None)

        result = output

        while cur1 and cur2:
            if cur1.val < cur2.val:
                result.next = ListNode(cur1.val)
                result = result.next
                cur1 = cur1.next
            else:
                result.next = ListNode(cur2.val)
                result = result.next
                cur2 = cur2.next

        while cur1:
            result.next = ListNode(cur1.val)
            result = result.next
            cur1 = cur1.next

        while cur2:
            result.next = ListNode(cur2.val)
            result = result.next
            cur2 = cur2.next
        output = output.next
        return output



