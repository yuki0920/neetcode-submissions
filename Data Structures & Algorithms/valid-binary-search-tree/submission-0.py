# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # leftのmax <= key <= rightのmin
        self.bst = True
        def dfs(node, key) -> (int, int):
            if not node:
                return (float('inf'), float('-inf'))
            
            left_min, left_max = dfs(node.left, node.val)
            right_min, right_max = dfs(node.right, node.val)

            if not left_max <= key or not key <= right_min:
                self.bst = False
            
            return (min(left_min, right_min, node.val), max(left_max, right_max, node.val))

        dfs(root, root.val)

        return self.bst


        