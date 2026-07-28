# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root:
            return res

        self.inorderHelper(root, res)
        
        return res
    
    def inorderHelper(self, root: Optional[TreeNode], res: List[int]):
        if root:
            self.inorderHelper(root.left, res)
            res.append(root.val)
            self.inorderHelper(root.right, res)