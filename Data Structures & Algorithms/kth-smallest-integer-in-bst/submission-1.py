# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 左から1番小さい値を求めていく
        # dfsでx番目と値を返す
        self.ans = None
        def dfs(node, xth) -> int:
            if node is None:
                return xth

            if xth == k:
                self.ans = node.val

            left = dfs(node.left, xth)
            if left == k:
                self.ans = node.val
                
            right = dfs(node.right, left+1)
            return right

        dfs(root, 1)
        return self.ans
