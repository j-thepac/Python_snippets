"""
230. Kth Smallest Element in a BST
Medium
Topics
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def append(self,i):
        if i is None:
            return
        if i <self.val:
            if not self.left:
                self.left=TreeNode(i)
            else:
                self.left.append(i)
        else:
            if not self.right:
                self.right=TreeNode(i)
            else:
                self.right.append(i)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l=[]
        def inorder(root):
            if not root:return
            l.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        l.sort()
        return l[k-1]

if (__name__=='__main__'):
    l =[3,1,4,None,2]     
    t=TreeNode(l[0])
    for i in l[1:]:
        t.append(i)

    sol=Solution()
    print(sol.kthSmallest(t,1))

