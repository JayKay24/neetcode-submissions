class Solution:
    def climbStairs(self, n: int) -> int:
        return self._climbRecursive(n, {})

    def _climbRecursive(self, n: int, memo: dict[int, int]) -> int:
        if n < 0:
            return 0
        if n == 1 or n == 0:
            return 1
        if n in memo:
            return memo[n]
    
        memo[n] = self._climbRecursive(n - 1, memo) + self._climbRecursive(n - 2, memo)

        return memo[n]
        