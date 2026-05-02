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
        def dfs(node) -> (int, int):
            if not node:
                return (float('inf'), float('-inf'))
            
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)

            if node.val <= left_max or right_min <= node.val:
                self.bst = False

            return (min(left_min, right_min, node.val), max(left_max, right_max, node.val))

        dfs(root)

        return self.bst


        