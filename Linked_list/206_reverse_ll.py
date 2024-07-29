class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        prev=None
        while current is not None:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
