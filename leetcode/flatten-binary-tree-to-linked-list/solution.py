# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        ns = []
        def deep(node,ns):
            if node.left:
                ns.append(node.left)
                deep(node.left,ns)
            if node.right:
                ns.append(node.right)
                deep(node.right,ns)
        
        if root:
            deep(root,ns)
            
        node = root
        for n in ns:
            node.left = None
            node.right = n
            node = node.right
