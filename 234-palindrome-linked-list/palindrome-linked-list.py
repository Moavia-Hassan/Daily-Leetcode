# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next
        
        return list1 == list1[::-1]



















        # curr = head
        # list1 = []
        # while curr != None:
        #     list1.append(curr.val)
        #     curr = curr.next
        # return list1 == list1[::-1]
