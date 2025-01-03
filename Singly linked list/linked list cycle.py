# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Brute force solution
class Solution:
    def hasCycle(self, head):
        temp = head
        node_set = set()  # here we use a set to store the nodes we have seen so far
        while temp:
            if temp in node_set:  # here we check if temp is present in the node
                return True
            node_set.add(temp.val)  # if not we add it to the set
            temp = temp.next
        return False


#  Optimal solution
class Solution:
    def hasCycle(self, head):
        temp = head
        slow = head
        fast = head
        while fast and fast.next:  # the loop runs until the linked list is traversed
            slow = slow.next  # this goes one step at a time
            fast = fast.next.next  # this goes two step at a time
            if slow == fast:  # here we check if slow is equal to fast
                return True
        return False


# Time complexity: O(n)
# Space complexity : O(1)
