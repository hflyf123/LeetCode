# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        result = 0
        begin_value = prices[0]
        for p in prices:
            if begin_value < p:
                result += p - begin_value
                begin_value = p
            else:
                begin_value = min(p, begin_value)
        return result
        
        
        