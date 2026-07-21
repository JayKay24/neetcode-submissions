class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        
        return self.recurse_cc(coins, amount, [float("inf")] * amount)

    def recurse_cc(self, coins: list[int], remainder: int, counter: list[float]) -> int:
        if remainder < 0:
            return -1
        if remainder == 0:
            return 0
        if counter[remainder - 1] != float("inf"):
            return counter[remainder - 1]
        
        minimum = float("inf")

        for coin in coins:
            result = self.recurse_cc(coins, remainder - coin, counter)
            if 0 <= result < minimum:
                minimum = 1 + result
        
        counter[remainder - 1] = minimum if minimum != float("inf") else -1

        return counter[remainder - 1]