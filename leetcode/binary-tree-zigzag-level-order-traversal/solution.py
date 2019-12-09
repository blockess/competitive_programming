# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        
        if not root:
            return []
        
        left = True
        children = [root]
        while children:
            values = []
            nodes = children[:]
            children = []
            for child in nodes:
                if not child: continue
                values.append(child.val)
                if child.left:
                    children.append(child.left)
                if child.right:
                    children.append(child.right)
            
            if not left:
                values = values[::-1]
                
            result.append(values)
            left = not left
            
        return result
