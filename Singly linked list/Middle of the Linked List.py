# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Brute
class Solution:
    def middleNode(self, head):
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        temp = head
        for i in range(n // 2):
            temp = temp.next
        return temp


# Optimal


class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
