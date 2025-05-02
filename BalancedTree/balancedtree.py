class Solution:
    def check(self, root):
        if not root:
            return 0
        l = self.check(root.left)
        if l == -1:
            return -1
        r = self.check(root.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1

    def isBalanced(self, root):
        return self.check(root) != -1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree=TreeNode(3)
tree.left=TreeNode(9)
tree.right=TreeNode(20)
tree.right.left=TreeNode(15)
tree.right.right=TreeNode(7)


s=Solution()

print(s.isBalanced(tree))
print(1)
#