class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_k_list(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        v_map = {}
        for l in lists:
            while l is not None:
                try:
                    v_map[l.val].append(l)
                except KeyError:
                    v_map[l.val] = [l]
                l = l.next
        head = last = ListNode(-1)
        for k in sorted(v_map.keys()):
            for t in v_map[k]:
                last.next = t
                last = t
        last.next = None
        return head.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]

    sol_obj = Solution()
    merged_head = sol_obj.merge_k_list(lists)
    print_linked_list(merged_head)
