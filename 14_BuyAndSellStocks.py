# First solution 9/26/2024 - 15 mins

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximum = 0

        l, r = 0, 1
        while r < len(prices):
            maximum = max(maximum, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l += 1
                r = l + 1
            else:
                r += 1

        return maximum


"""
Time: O(n)
Space: O(1)
Attempts: Had to watch video for theory (First Sliding Window)

Mistakes made:
- Was thinking subarray rather than two pointers sliding
- Could skip steps by doing l=r when if prices[l] > prices[r] because we know that will be the minimum instead of stepping through to it

Learned:
Finding largest min to max is two pointers sliding through

"""