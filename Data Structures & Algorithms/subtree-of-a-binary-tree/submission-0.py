# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # すべてのノードごとにサブツリーかどうかを判定する

        def is_same(a, b) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            return is_same(a.left, b.left) and is_same(a.right, b.right)

        def dfs(node) -> bool:
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right or is_same(node, subRoot)

        return dfs(root)


        
            