# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodelist=ListNode()
        curr=nodelist
        carry=0
        if l1.next is None and l2.next is None:
            n=l1.val+l2.val
            curr.next=ListNode(n%10)
            curr=curr.next
            carry=n//10
            if carry:
                curr.next=ListNode(1)
                curr=curr.next
                
            return nodelist.next
        if l1.next is None and l1.val==0:
            return l2
        if l2.next is None and l2.val==0:
            return l1
        
        while l1 or l2:
            if l1 and l2:
                n=(l1.val+l2.val+carry)
                l1=l1.next
                l2=l2.next
            elif l1:
                n=l1.val+carry
                l1=l1.next
            else:
                n=l2.val+carry
                l2=l2.next
            curr.next=ListNode(n%10)
            carry=n//10
            curr=curr.next
        if carry:
            curr.next=ListNode(1)
            curr=curr.next
        return nodelist.next
        
    
        
