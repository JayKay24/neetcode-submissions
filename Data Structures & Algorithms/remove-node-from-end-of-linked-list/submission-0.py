# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leader = head
        follower = head

        for i in range(n):
            leader = leader.next

            if leader is None:
                return head.next
        
        while leader.next is not None:
            leader = leader.next
            follower = follower.next

        follower.next = follower.next.next

        return head