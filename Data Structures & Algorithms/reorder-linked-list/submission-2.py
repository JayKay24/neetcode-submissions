# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        prev, middle_node = self.get_middle_node(head)
        prev.next = None
        reversed_middle_node = self.reverse_linked_list(middle_node)

        self.get_merged_linked_list(head, reversed_middle_node)

    def get_middle_node(self, ll: ListNode) -> ListNode:
        slow = fast = ll
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        return (prev, slow)

    def reverse_linked_list(self, ll: ListNode) -> ListNode:
        prev = None
        current = ll

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

    def get_merged_linked_list(self, ll_1: ListNode, ll_2: ListNode) -> ListNode:
        current = ll_1

        while current.next:
            next_node, current.next = current.next, ll_2
            current = next_node
            ll_2_next, ll_2.next = ll_2.next, current
            ll_2 = ll_2_next
        
        current.next = ll_2

        return ll_1