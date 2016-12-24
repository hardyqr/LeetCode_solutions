# Freddy/Fangyu@BNU
# 12/25/2016


'''Solution 1'''
def digger(root,count):
    if root.left is not None and root.right is None:
        count+=1
        return digger(root.left,count)
    if root.right is not None and root.left is None:
        count+=1
        return digger(root.right,count)
    if root.right is not None and root.left is not None:
        count+=1
        return max(digger(root.right,count),digger(root.left,count))
    else:
        return count
class Solution(object):
    def maxDepth(self, root):
        if root==None:return 0
        return digger(root,1)

'''Solution 2'''
'''DFS, a more compact way'''
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
