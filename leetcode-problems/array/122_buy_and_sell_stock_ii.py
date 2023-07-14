# You are given an integer array prices where prices[i] is the price
# of a given stock on the ith day.

# on each day, you may decide to buy and/or sell the stock. You can
# only hold at most one share of the stock at any time. However,
# you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5 - 1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6 - 3 = 3.
# Total profit = 4 + 3 = 7.

# Time: O(n)
# Space: O(1)
class Solution:
    def max_profit(self, prices: list[int]) -> int:
        i = 0
        j = 0
        profit = 0
        while i < len(prices) - 1:
            if prices[i] > prices[i + 1]:
                i += 1
            else:
                j = i + 1
                while j < len(prices):
                    if j == len(prices) - 1:
                        break
                    if prices[j] < prices[j + 1]:
                        j += 1
                    else:
                        break
                profit += prices[j] - prices[i]
                i = j + 1
        return profit

solution = Solution()
print(solution.max_profit([7, 1, 5, 3, 6, 4])) # 7
print(solution.max_profit([1, 2, 3, 4, 5])) # 4
print(solution.max_profit([7, 6, 4, 3, 1])) # 0