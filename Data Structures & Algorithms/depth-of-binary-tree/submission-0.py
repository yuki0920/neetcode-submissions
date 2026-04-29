# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def dfs(node, depth):
            if not node:
                return depth

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

            self.depth = max(self.depth, depth)

        dfs(root, 1)

        return self.depth