# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True  # Both nodes are None
            if not t1 or not t2:
                return False  # Only one of the nodes is None
            return (t1.val == t2.val and
                    is_mirror(t1.left, t2.right) and
                    is_mirror(t1.right, t2.left))

        return is_mirror(root, root)
        