# March 24, 2018 @M3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = queue.Queue()
        q.put(root)
        u = None
        while not q.empty():
          u = q.get()
          if (u.right): q.put(u.right)
          if (u.left): q.put(u.left)
        return u.val
