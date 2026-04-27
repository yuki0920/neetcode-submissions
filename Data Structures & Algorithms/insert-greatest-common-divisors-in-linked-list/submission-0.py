# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if a < b:
                a, b = b, a

            mod = a % b
            if mod == 0:
                return b
            else:
                return gcd(b, mod)


        # 挿入時の操作currentを挿入するノードとすると、current.next = node, node.next = next
        current = head
        while current.next:
            node = ListNode()
            node.val = gcd(current.val, current.next.val)
            node.next = current.next
            current.next = node

            current = node.next

        return head
            
        
        