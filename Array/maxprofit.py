class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices)-1):
            if prices[i] >= prices[i+1]:
                continue
            else:
                sum += prices[i+1] - prices[i]
        return sum

prices = [1,2,3,4,5]

print Solution().maxProfit(prices=prices)
