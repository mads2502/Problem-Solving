# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        return self.helper(head,k)
    
    def helper(self,h,k):
        curr=h
        ptr1=ptr2=curr
        cnt=1
        while(curr is not None):
            if cnt==k:
                val=curr.val
                #print("yesd")
                ptr1=curr
            cnt+=1
            curr=curr.next
        curr1=h
        cnt1=1
        #print(cnt)
        while(curr1 is not None):
            if cnt1==cnt-1-k+1:
                #print("yes")
                ptr2=curr1
                break
            cnt1+=1
            curr1=curr1.next
        ptr1.val,ptr2.val=ptr2.val,ptr1.val
        return h
        
        
