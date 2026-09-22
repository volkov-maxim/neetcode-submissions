# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRoot_flatened = self.tree2list(subRoot)
        check_list = [root]

        while check_list:
            node = check_list.pop()
            if node.val == subRoot.val:
                root_flatened = self.tree2list(node)
                if root_flatened == subRoot_flatened: return True
            if node.left:
                check_list.append(node.left)
            if node.right:
                check_list.append(node.right)
        
        return False

    
    def tree2list(self, root: Optional[TreeNode]) -> list:
        if not root: return None

        left = self.tree2list(root.left)
        right = self.tree2list(root.right)

        return [root.val, left, right]