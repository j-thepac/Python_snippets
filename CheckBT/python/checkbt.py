# Definition for a binary tree node.

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def  append(self,i):
        if i<self.val:
            if not self.left:self.left=TreeNode(i)
            else:self.left.append(i)
        else:
            if not self.right:self.right=TreeNode(i)
            else:self.right.append(i)

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def fn(rt):
            if not rt: return 
            if rt.left:
                if rt.val> rt.left.val:fn(rt.left)
                else: return False
            if rt.right:
                if rt.val< rt.right.val:fn(rt.right)
                else:return False
            return

        return True if fn(root) ==None  else False

# root = [5,1,4,None,None,3,6] #[2,1,3]
# n=TreeNode(root[0])
# for i in root[1:]:
#     n.append(i)
    

n=TreeNode(5)
n.left=TreeNode(1)
n.right=TreeNode(4)

s=Solution()
print(s.isValidBST(n))
