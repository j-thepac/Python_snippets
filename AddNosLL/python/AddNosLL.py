"""
2. Add Two Numbers
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self,i):
        if(self.next)==None : self.next=ListNode(i)
        else: self.next.append(i)

class Solution:
    firstRun=None
    resultList=[]
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        res=None
        resultList=[]
        while l1 or l2 or carry:
            if(l1!=None):
                v1=l1.val
                l1=l1.next
            else:
                v1=0
            
            if(l2!=None):
                v2=l2.val
                l2=l2.next
            else:
                v2=0

            temp_res=v1+v2+carry
            carry=temp_res//10
            sm= temp_res % 10
            res=self.createResult(sm,res)
            resultList.append(sm)
        resultList.append(carry)
        self.resultList=resultList
        return res

    def createResult(self,i,res):
        if(self.firstRun == None):
            self.firstRun=True
            return ListNode(i)
        if res.next==None: res.next=ListNode(i)
        else: self.createResult(i,res.next)
        return res

# l1 = [2,4,3]
# ll1=ListNode(2)
# ll1.append(4)
# ll1.append(3)


# l2 = [5,6,4]
# ll2=ListNode(5)
# ll2.append(6)
# ll2.append(4)
# sol=Solution()
# res= sol.addTwoNumbers(ll1,ll2) #passing linked list not list
# print(sol.resultList)



