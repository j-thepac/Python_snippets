
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr=head
        s={curr.val}
        def nxt(n):
            if n==None:return
            elif n.val not in s:
                s.add(n.val)
                return n
            elif n.val in s:return nxt(n.next) 

        while curr and curr.next :
            curr.next=nxt(curr.next)
            curr=curr.next
        return head
                
n=ListNode(1)
n.next=ListNode(1)
n.next.next=ListNode(2)
n.next.next.next=ListNode(3)
n.next.next.next.next=ListNode(3)


s=Solution()
res = s.deleteDuplicates(n)
print(res.val)
print(res.next.val)
print(res.next.next)