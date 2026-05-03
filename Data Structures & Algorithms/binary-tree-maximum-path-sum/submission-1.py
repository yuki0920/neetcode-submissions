# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        # 辺の最大値を返す
        def dfs(node) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            print(node.val, left, right)

            self.max_sum = max(self.max_sum, left+right+node.val, node.val)

            return max(left, left+node.val, right, right+node.val, node.val)

        dfs(root)

        return self.max_sum