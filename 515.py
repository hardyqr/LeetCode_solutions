# March 31, 2018 @M3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        max_val = 0
        n = 0
        qa = []
        qa.append(root)
        if root is None: # if empty
          return res
        while qa:
          qb = []
          max_val= qa[0].val
          for u in qa:
            max_val = max(max_val, u.val)
            if (u.right): qb.append(u.right)
            if (u.left): qb.append(u.left)
          res.append(max_val)
          qa = qb
        return res
