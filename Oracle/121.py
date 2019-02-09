#best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices==None or len(prices)==0:
            return 0
        cur = 0
        m = 0
        cur = prices[0]
        for i in range(1,len(prices)):
            if prices[i] - cur >0:
                m = max(m, prices[i] - cur)
            else:
                cur = prices[i]
        return m
# use cur to store the buy time
