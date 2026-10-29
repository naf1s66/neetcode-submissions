# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        # First traversal: count nodes
        while current is not None:
            count += 1
            current = current.next

        # Zero-based index of node to remove
        desired = count - n

        # Special case: remove first node
        if desired == 0:
            head = head.next
            return head

        # Second traversal
        current = head

        # Move to the node before the target
        for i in range(desired - 1):
            current = current.next

        # Skip the target node
        current.next = current.next.next

        return head