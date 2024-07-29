class Solution(object):
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = last = last2 = head
        while current is not None:
            nex = current.next
            if current == last.next:
                last.next = nex
                current.next = last
                if last == head:
                    head = current
                else:
                    last2.next = current
                last2 = last
                last = nex
            current = nex
        return head
