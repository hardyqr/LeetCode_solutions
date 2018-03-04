# March 3rd, 2018 @DP
def mt(t1,t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    t1.val += t2.val
    t1.left = mt(t1.left,t2.left)
    t1.right = mt(t1.right,t2.right)
    return t1
class Solution:
    def mergeTrees(self, t1, t2):
        return mt(t1,t2)

        
