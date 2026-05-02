# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(node, max_num):
            if not node:
                return
            if node.val  >= max_num:
                self.counter += 1

            max_num = max(max_num, node.val)

            dfs(node.left, max_num)
            dfs(node.right, max_num)

        dfs(root, float('-inf'))

        return self.counter