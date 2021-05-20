# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nstride=curr=head
        for i in range(0,n):
            nstride=nstride.next
            #place a pointer n places away from start
        while nstride:
            if nstride.next==None:
                #for valid n steps within range remove the corresponding element
                p=curr.next
                q=curr
                q.next=p.next
                break
            nstride=nstride.next
            curr=curr.next
        if nstride==None:
            #if in case the stride pointer is None then target has been reached 
            #The target to be removed would be curr
            return curr.next
        return head
