class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        left=root.left
        right=root.right
        node=left
        while node and node.right:
            node=node.right
        root.left=None
        if left:
            root.right=left
            node.right=right
        else:
            root.right=right