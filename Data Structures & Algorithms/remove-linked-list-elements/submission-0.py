# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Remove matching nodes from the beginning
        while head is not None and head.val == val:
            head = head.next

        current = head

        # Traverse the remaining linked list
        while current is not None and current.next is not None:

            # Remove consecutive matching nodes
            while current.next is not None and current.next.val == val:
                current.next = current.next.next

            current = current.next

        return head
        