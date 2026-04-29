# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # have persistent data for the longest length
        self.ans = 0

        
        # helper function dfs in order to find the depth of the tree
        def maxDepth(node):
        
            # base case if no nodes return None
            if not node:
                return 0

            # recursively get depth of left/right subtrees
            leftDepth = maxDepth(node.left)
            rightDepth = maxDepth(node.right)

            # update the global max diameter
            self.ans = max(self.ans, leftDepth + rightDepth)

            # return the height of current node
            return 1 + max(leftDepth, rightDepth)
            
        maxDepth(root)
        return self.ans
