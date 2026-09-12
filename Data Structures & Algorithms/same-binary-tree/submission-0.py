# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def tree2list(root) -> list:
            if not root: return root

            left = tree2list(root.left)
            right = tree2list(root.right)

            return [root.val, left, right] 

        return tree2list(p) == tree2list(q)