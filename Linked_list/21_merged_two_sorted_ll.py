class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def merge_two_lists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2

def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

l1 = create_linked_list([1, 2, 5])
print(l1)
l2 = create_linked_list([1, 3, 4])
print(l2)

# Merge the two lists
solution_obj= Solution()
merged_list = solution_obj.merge_two_lists(l1, l2)
print(merged_list)
