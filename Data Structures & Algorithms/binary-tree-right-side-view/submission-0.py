# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        current_level = 1
        que = deque([(root, current_level)])
        ans = []

        while que:
            node, level = que.popleft()

            if level > current_level:
                current_level += 1
                ans.append(right)

            right = node.val

            if node.left:
                que.append((node.left, level+1))
            if node.right:
                que.append((node.right, level+1))

        ans.append(right)

        return ans
