# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        current_level = 1
        que = deque([(root, current_level)])
        ans = []
        current = []

        while que:
            node, level = que.popleft()
            if level > current_level:
                ans.append(current)
                current_level += 1
                current = []
            
            current.append(node.val)

            if node.left:
                que.append((node.left, level+1))
            if node.right:
                que.append((node.right, level+1))

        ans.append(current)
            
        return ans