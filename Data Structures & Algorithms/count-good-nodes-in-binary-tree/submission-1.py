# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_num):
            if not node:
                return 0

            current = 0
            if node.val  >= max_num:
                current = 1

            max_num = max(max_num, node.val)

            left = dfs(node.left, max_num)
            right = dfs(node.right, max_num)

            return current + left + right

        return dfs(root, float('-inf'))