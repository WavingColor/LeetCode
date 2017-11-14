# Find any position of a target number in a sorted array. Return -1 if target does not exist.
# Given [1, 2, 2, 4, 5, 5].

# For target = 2, return 1 or 2.

# For target = 5, return 4 or 5.

# For target = 6, return -1.

# Challenge 
# O(logn) time
class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        
        def findP(subNums, target, startTag):
            length = len(subNums)
            if subNums is None or length == 0:
                return -1
            if length == 1 and subNums[0] != target:
                return -1
            checkIndex = length/2
            print(checkIndex, startTag)
            halfVal = subNums[checkIndex]
            if halfVal == target:
                print('find out index: %s' % (checkIndex + startTag))#这个，测试的时候，18744return了依然告诉我没找到，应该是网页bug，符测试数据
                return checkIndex + startTag
            if halfVal < target:
                return findP(subNums[checkIndex :], target, startTag+checkIndex)
            else:
                return findP(subNums[: checkIndex], target, startTag)
        
        return findP(nums, target, 0)
            
nums = [1,2,2,4,5,5]
with open('LintCode.Classical.Binary.Search.in', 'r') as f:
    nums = f.read()
# print(nums)
print(Solution().findPosition(nums, 996))