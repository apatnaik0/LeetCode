# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bt(self,nums,s,e):

        if s > e:
            return None

        mid = (s+e)//2
        root = TreeNode(nums[mid])

        root.left = self.bt(nums,s,mid-1)
        root.right = self.bt(nums,mid+1,e)

        return root


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.bt(nums,0,len(nums)-1)