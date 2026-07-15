class Solution:
    def permute(self, nums: List[int], l=0) -> List[List[int]]:
        n = len(nums)
        if l >= n - 1:
            return [[nums[l]]]
        
        head = nums[l]
        tail_perms = self.permute(nums, l + 1)

        permutations = []

        for perm in tail_perms:
            for i in range(len(perm) + 1):
                new_perm = perm[0:i] + [head] + perm[i:]
                permutations.append(new_perm)
        
        return permutations
        