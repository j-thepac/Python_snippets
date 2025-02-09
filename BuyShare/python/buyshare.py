


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices)==1:return 0 
        p1,p2,profit=0,1,0
        while p1<p2 and p2<len(prices)-1:
            if prices[p1]<prices[p2] and prices[p2]<=prices[p2+1]:
                p2+=1
            elif prices[p1]<prices[p2] and prices[p2]>prices[p2+1]:
                profit=profit+(prices[p2] - prices[p1] )
                p1=p2
                p2+=1
            else:
                p1+=1
                p2+=1
        if prices[p2] > prices[p1]: profit = profit+( prices[p2] - prices[p1])
        return profit


# sol=Solution()
# print(sol.maxProfit(prices =[5,2,3,2,6,6,2,9,1,0,7,4,5,0]))