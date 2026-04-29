# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        que = deque([root])

        while que:
            node = que.popleft()
            if node.left and node.right:
                node.left, node.right = node.right, node.left
                que.append(node.left)
                que.append(node.right)
            elif node.left:
                node.right = node.left
                que.append(node.right)
            elif node.right:
                node.left = node.right
                que.append(node.left)

        return root