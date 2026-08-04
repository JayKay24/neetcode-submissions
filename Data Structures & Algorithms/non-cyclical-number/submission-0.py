class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_square_digits(n)

        while fast != 1 and slow != fast:
            slow = self.sum_square_digits(slow)
            fast = self.sum_square_digits(self.sum_square_digits(fast))
        
        return fast == 1 or slow == 1

    def sum_square_digits(self, n: int) -> int:
        sum_digits = 0

        while n > 0:
            sum_digits += ((n % 10) ** 2)
            n //= 10

        return sum_digits
            