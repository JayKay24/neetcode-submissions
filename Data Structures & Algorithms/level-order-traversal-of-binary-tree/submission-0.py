# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue: deque[TreeNode] = deque()
        queue.append(root)

        while len(queue) > 0:
            q_size = len(queue)
            level_order: list[int] = []


            for _ in range(q_size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
                level_order.append(current.val)
            
            result.append(level_order)
        
        return result
        