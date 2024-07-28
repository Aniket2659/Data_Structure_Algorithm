class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_num(self, l1, l2):
        carry = 0
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = int(val / 10)
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next

def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    solution_obj = Solution()
    result = solution_obj.add_two_num(l1, l2)
    print_linked_list(result)
