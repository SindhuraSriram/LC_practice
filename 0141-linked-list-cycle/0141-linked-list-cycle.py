# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Traverse the linked list
        while fast and fast.next:
            slow = slow.next           # Move slow pointer by 1 step
            fast = fast.next.next      # Move fast pointer by 2 steps

            # If slow and fast pointers meet, a cycle exists
            if slow == fast:
                return True

        # If we reach the end of the list, there is no cycle
        return False
        