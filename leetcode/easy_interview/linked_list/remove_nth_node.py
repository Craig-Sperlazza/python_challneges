# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev_node = head
        count = 0

        while node.val != None:
            count += 1
        for _ in range(count - n):
            prev_node.val = node.val
            prev_node.next = node.next
            node.next = node.next.next
            node.val = node.next.val
        
        prev_node.val = node.next.val
        prev_node.next = node.next.next
        






        # #if first node is removed
        # if head.val == n and count == 0:
        #     head.val = head.next.val
        #     head.next = head.next.next
        # else:
        #     while node.next != None:
        #         prev_node.val = node.val
        #         prev_node.next = node.next
        #         node.next = node.next.next
        #         node.val = node.next.val

        #         if node.val == n:
        #             prev_node.val = node.next.val
        #             prev_node.next = node.next.next
        #             node.val = None
        #             node.next = None
        #     return None





