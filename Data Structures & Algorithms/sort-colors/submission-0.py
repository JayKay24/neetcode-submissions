class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        l, s, r = 0, 0, n - 1

        while s <= r:
            if nums[s] == 0:
                self.swap(nums, s, l)
                l += 1
                s += 1
            elif nums[s] == 2:
                self.swap(nums, s, r)
                r -= 1
            else:
                s += 1
    
    def swap(self, arr: list[int], idx1: int, idx2: int) -> None:
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]