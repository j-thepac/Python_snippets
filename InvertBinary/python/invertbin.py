'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def append(self,i):
        if(i<self.val):
            if(self.left is None):self.left=TreeNode(i)
            else:self.left.append(i)
        else:
            if(self.right is None):self.right=TreeNode(i)
            else:self.right.append(i)


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:return None          
        tree=TreeNode(root.val)
        tree.left=self.invertTree(root.right)
        tree.right=self.invertTree(root.left)
        return tree



l=[4,2,7,1,3,6,9]
tree=TreeNode(l[0])
tree.left=TreeNode(2)
tree.right=TreeNode(7)
tree.left.left=TreeNode(1)
tree.left.right=TreeNode(3)

tree.right.left=TreeNode(6)
tree.right.right=TreeNode(9)


s=Solution()
res= s.invertTree(tree)
print("wait")
