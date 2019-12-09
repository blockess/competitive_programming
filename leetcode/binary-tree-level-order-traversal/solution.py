# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        def append_to_result(value, depth):
            nonlocal result
            
            if len(result) < depth+1:
                result.append([])
                
            result[depth].append(value)
        
        def walk(node, depth):
            if node.left:
                append_to_result(node.left.val, depth)
                walk(node.left, depth+1)
            
            if node.right:
                append_to_result(node.right.val, depth)
                walk(node.right, depth+1)
        
        if root:
            result.append([root.val])
            walk(root, 1)
        
        return result
