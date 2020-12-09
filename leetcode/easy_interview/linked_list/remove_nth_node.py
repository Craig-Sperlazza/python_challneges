# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        prev = head
        node_count = head
        count = 1

        while node_count.next != None:
            count += 1
            node_count = node_count.next
        i = 1
        while i <= (count - n):
            prev = first
            first = first.next
            i += 1

        prev.next = first.next
        first.next = first.next
        first.val = first.next.val
        return first

        
def removeNthFromEnd(self, head, n):
    #if there is no node after head
    if not head.next:
        return None

    front = head
    back = head
    counter = 0
    flag = False
    while counter <= n:
        if(not front):
            flag = True
            break
        front = front.next
        counter += 1
    while front:
        front = front.next
        back = back.next
    if not flag:
        temp = back.next
        back.next = temp.next
        temp.next = None
    else:
        head = head.next
    return head
        






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





