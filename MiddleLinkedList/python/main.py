class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def append(self,i):
        if not self.next:
            self.next=ListNode(i)
        else:
            self.next.append(i)


class Solution():
    def middleNode(self, head: ListNode) -> ListNode:
        l=[]
        def getList(node):
            if not(node):return
            else:
                l.append(node.val)
                return getList(node.next)
        def createList(root,i):
            if not(root.next):
                root.next =  ListNode(i)
                return root
            else:
                return createList(root.next,i)
        getList(head)
        m=len(l)//2
        returnList=l[m+1:]
        root= ListNode(l[m])
        for i in returnList:
            createList(root,i)
        return root



l=[65,66,26,77,96,86,11,21,13,80]
node=ListNode(l[0])
for i in l[1:]:
    node.append(i)

s=Solution()
res=s.middleNode(node)
lres=[]
while (res):
    lres.append(res.val)
    res=res.next
assert(lres==[86,11,21,13,80])
