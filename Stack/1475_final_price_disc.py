class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []
        for i, v in enumerate(prices):
            ans.append(v)
            for j in range(i + 1, len(prices)):
                if prices[j] <= v:
                    ans[-1] -= prices[j]
                    break
        return ans
