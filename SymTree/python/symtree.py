


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not(root.left) and not(root.right):return True
        elif (not(root.left) and root.right) and  (not(root.right) and root.left): return False

        def BFS(root):
            q=[root]
            res=[]
            while q:
                t=q.pop(0)
                res.append(t.val)
                if t.left: q.append(t.left)
                elif t.right:q.append(t.right)
            return res
        return BFS(root.left) == BFS(root.right)   

l=[1,2,2,3,4,4,3]
t1=TreeNode(l[0])
t1.left=TreeNode(l[1])
t1.right=TreeNode(l[2])

s=Solution()
s.isSymmetric(t1)