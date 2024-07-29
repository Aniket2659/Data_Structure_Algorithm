# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count==1:
            head=None
            tail=None
            return head
        elif n == count:
            return head.next

        else:
            current=head
            for i in range((count-n)):
                current=current.next
            previous=head
            for i in range((count-n)-1):
                previous=previous.next
            previous.next=current.next
            current.next=None

            return head

    
        