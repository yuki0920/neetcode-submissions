# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfsで子孫を上に返していく
        self.lca = None

        def dfs(node) -> list(int):
            if not node:
                return []
            left = dfs(node.left)
            right = dfs(node.right)
            total = [node.val] + left + right

            if not self.lca and p.val in total and q.val in total:
                self.lca = node

            return total

        dfs(root)
        return self.lca