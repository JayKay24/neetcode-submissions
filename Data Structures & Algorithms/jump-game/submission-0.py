class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target_num_idx = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= target_num_idx:
                target_num_idx = i
        
        if target_num_idx == 0:
            return True
        return False