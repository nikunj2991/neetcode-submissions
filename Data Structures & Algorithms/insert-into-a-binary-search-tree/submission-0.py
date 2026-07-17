# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root

        if val > curr.val:
            if not curr.right:
                curr.right = TreeNode(val)
            else:
                curr = curr.right
                self.insertIntoBST(curr, val)
        elif val < curr.val:
            if not curr.left:
                curr.left = TreeNode(val)
            else:
                curr = curr.left
                self.insertIntoBST(curr, val)

        return root
