from collections import deque
class MinStack:

    def __init__(self):self.q=deque()
        
    def push(self, val: int) -> None:self.q.append(val)

    def pop(self) -> None:self.q.pop()

    def top(self) -> int:return list(self.q)[-1]

    def getMin(self) -> int:return min(self.q)

class MinStack2:
    def __init__(self):self.l=[]   

    def push(self, val: int) -> None:self.l.append(val)
        
    def pop(self) -> None:self.l.pop(-1)

    def top(self) -> int:return self.l[-1]
        
    def getMin(self) -> int:
        return min(self.l)
        

# -3 , 0 ,-2
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
     

minStack =  MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); # return -3
minStack.pop();
minStack.top();    # return 0
minStack.getMin(); # return -2
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()