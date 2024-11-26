# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None:
            return head
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next   
        k = k % len(arr)

        arr = arr[-k:] + arr[:-k] 
        dummy = ListNode()
        temp = dummy
        for val in arr:
            temp.next = ListNode(val)
            temp = temp.next
        return dummy.next
        
        