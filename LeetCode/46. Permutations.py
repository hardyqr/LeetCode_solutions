# Freddy/Fangyu
# 12/17/2016
'''Solution 1'''
import itertools
class Solution(object):
    def permute(self, nums):
        aws=[]
        for i in itertools.permutations(nums):
            aws.append(list(i))
        return aws
'''Solution 2'''

class Solution(object):
    def permute(self, nums):
        if len(nums) <=1:
            yield elements
        else:
            for j in permute(self,nums[1:]):
                for i in range(len(nums)):
                    # nb elements[0:1] works in both string and list contexts
                    yield j[:i] + nums[0:1] + j[i:]
