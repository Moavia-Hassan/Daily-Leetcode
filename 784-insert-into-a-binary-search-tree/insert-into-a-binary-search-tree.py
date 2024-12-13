# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
    
        new_node = TreeNode(val)
        if not root:
            return new_node
        
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = new_node
                    break
                else:
                    node = node.right
            elif val < node.val:
                if not node.left:
                    node.left = new_node
                    break
                else:
                    node = node.left
            else:
                break
        return root