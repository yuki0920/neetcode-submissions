# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_que = deque([p])
        q_que = deque([q])

        while p_que and q_que:
            pn = p_que.popleft()
            qn = q_que.popleft()

            if pn.val != qn.val:
                return False

            if pn.left and not qn.left:
                return False
            if pn.right and not qn.right:
                return False
            if qn.left and not pn.left:
                return False
            if qn.right and not pn.right:
                return False

            if pn.left and qn.left:
                p_que.append(pn.left)
                q_que.append(qn.left)
            if pn.right and qn.right:
                p_que.append(pn.right)
                q_que.append(qn.right)

        return True
            