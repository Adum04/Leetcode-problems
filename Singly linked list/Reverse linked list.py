# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Brute
class Solution:
    def reverseList(self, head):
        temp = head
        lis = []
        while temp:
            lis.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            ele = lis.pop()
            temp.val = ele
        return head


# Time: O(n), Space: O(n)


# Optimal
class Solution:
    def reverseList(self, head):
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
