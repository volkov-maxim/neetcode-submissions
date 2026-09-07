# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        seen = [root]
        node_h_d = {None: (0, 0)}

        while seen:
            node = seen[-1]
            if node.left and (node.left not in node_h_d):
                seen.append(node.left)
            elif node.right and (node.right not in node_h_d):
                seen.append(node.right)
            else:
                node = seen.pop()

                left_height, left_diameter = node_h_d[node.left]
                right_height, right_diameter = node_h_d[node.right]

                node_h_d[node] = (
                    1 + max(left_height, right_height),
                    max(left_height + right_height, left_diameter, right_diameter)
                )
            
        return node_h_d[root][1]