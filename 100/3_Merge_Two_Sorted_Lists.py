'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def append(self,i):
        if(self.next is None):self.next=ListNode(i)
        else: self.next.append(i)

    def show(self):
        print(self.val)
        if(self.next):self.next.show()

list1 = [1,2,4]
list2 = [1,3,4]

n1=ListNode(1)
n2=ListNode(1)

for i in list1[1:]:n1.append(i)
for i in list2[1:]:n2.append(i)

# n1.show()
# n2.show()
    
class Solution:
    res=None
    ptr=None
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:return list2
        elif list2 is None: return list1
        elif list1.val == list2.val:
            if(self.res==None):
                self.res=ListNode(list1.val)
                self.ptr=self.res 
            else:
                self.ptr.next=ListNode(list1.val)
                self.ptr=self.ptr.next
            self.mergeTwoLists(list1.next,list2.next)
        elif list1.val < list2.val:
            if(self.res==None):
                self.res=ListNode(list1.val)
                self.ptr=self.res 
            else:
                self.ptr.next=ListNode(list1.val)
                self.ptr=self.ptr.next
            self.mergeTwoLists(list1.next,list2)
        else:
            if(self.res==None):
                self.res=ListNode(list2.val)
                self.ptr=self.res
            else:
                self.ptr.next=ListNode(list2.val)
                self.ptr=self.ptr.next
            self.mergeTwoLists(list1,list2.next)
            

sol=Solution()
sol.mergeTwoLists(n1,n2)
sol.res.show()