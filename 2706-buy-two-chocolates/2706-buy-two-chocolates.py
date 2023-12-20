class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # sort, pick minimum and check if it's positive leftover. if yes return, if not return money
        prices.sort()
        if len(prices) < 2:
            choco = prices[0]
        else:
            choco = prices[0] + prices[1]
        leftover = money - choco
        if leftover >= 0:
            return leftover
        else:
            return money