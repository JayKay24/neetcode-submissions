# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q: deque[TreeNode] = deque()
        q.append(root)

        while len(q) > 0:
            current = q.popleft()
            if current.val == subRoot.val:
                if self.isSame(current, subRoot):
                    return True
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        
        return False


    
    def isSame(self, a: TreeNode | None, b: TreeNode | None) -> bool:
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)