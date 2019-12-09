# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        
        def traverse(node, current_sum, path):
            nonlocal paths
            if not node.right and not node.left:
                if current_sum == sum:
                    paths.append(path)
            else:
                if node.right:
                    traverse(node.right, current_sum + node.right.val, path[:] + [node.right.val])
                if node.left:
                    traverse(node.left, current_sum + node.left.val, path[:] + [node.left.val])
        if root:
            traverse(root, root.val, [root.val])
        
        return paths
