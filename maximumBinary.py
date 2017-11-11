# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
           dummy = TreeNode(None)
        def d(root, nums):#递归调用，不断拆分，
            if not nums:
                return 
            i = nums.index(max(nums))
            root.val = max(nums)
            if nums[:i]:
                root.left = TreeNode(None)
                d(root.left, nums[:i])
            if nums[i+1:]:
                root.right = TreeNode(None)
                d(root.right, nums[i+1:])
        d(dummy, nums)
        return dummy
        # if nums is None:
        #     return None
        # if len(nums) == 0:
        #     return None
    
        # rootTree = TreeNode(max(nums))
        # leftTree = TreeNode(nums[0])
        # for i in range(1, len(nums)):#left
        #     if nums[i] == rootTree.val:
        #         break
        #     tmpTree = TreeNode(nums[i])
        #     if leftTree.val > tmpTree.val:
        #         leftTree.right = tmpTree
        #     else:
        #         tmpTree.left = leftTree
        #         leftTree = tmpTree
           
        
        # rightTree = TreeNode(nums[len(nums) -1])
        # for i in range(len(nums), 1,-1):
        #     if nums[i] == rootTree.val:
        #         break
        #     tmpTree = TreeNode(nums[i])
        #     if rightTree.val > tmpTree.val:
        #         rightTree.left = tmpTree
        #     else:
        #         tmpTree.left = rightTree
        #         rightTree = tmpTree
        
        # rootTree.left = leftTree
        # rootTree.right = rightTree
        # return rootTree
nums = [3,2,1,6,0,5]

print(Solution().constructMaximumBinaryTree(nums))
            
            
        