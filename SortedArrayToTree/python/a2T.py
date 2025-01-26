'''
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
'''
from typing import Optional
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def append(self ,i):
        if(i<self.val):
            if self.left:self.left.append(i)
            else: self.left=TreeNode(i)
        else:
            if self.right:self.right.append(i)
            else: self.right=TreeNode(i)

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if nums is None: return
        m=len(nums)//2
        t=TreeNode(nums[m])
        t.left=self.sortedArrayToBST(nums[0:m])
        t.right=   self.sortedArrayToBST(nums[m+1:])
        return t     

l=[-10,-3,0,5,9]       
s=Solution()
res=s.sortedArrayToBST(l)
print("hi")
