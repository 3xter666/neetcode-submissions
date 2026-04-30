# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        mp = {}
        cur = head
        while cur.next is not None:
            if cur in mp :
                return True
            mp[cur] = 1
            cur = cur.next
        return False