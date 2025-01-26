# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():

    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            temp= 1 + max(self.maxDepth(root.left) ,  self.maxDepth(root.right) )
            return temp


#Input: root = [3,9,20,null,null,15,7]

tree=TreeNode(3)
tree.left=TreeNode(9)
tree.right=TreeNode(20)
tree.right.left=TreeNode(15)
tree.right.right=TreeNode(7)


# tree=TreeNode(3)
# tree.left=TreeNode(9)



sol=Solution()
print(sol.maxDepth(tree))