class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct_idx = nums[i]
            if nums[i] < n and nums[i] != nums[correct_idx]:
                self.swap(nums, i, correct_idx)
            else:
                i += 1
        
        for j in range(n):
            if nums[j] != j:
                return j
        
        return n

    def swap(self, arr: list[int], x: int, y: int) -> None:
        arr[x], arr[y] = arr[y], arr[x]
