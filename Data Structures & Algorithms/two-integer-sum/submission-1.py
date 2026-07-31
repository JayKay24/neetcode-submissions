class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        result = [-1, -1]
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in seen:
                result[0], result[1] = i, seen[complement]
                return self.get_formatted_result(result)
            seen[nums[i]] = i
        
        return result

    def get_formatted_result(self, result: list[int]) -> list[int]:
        if result[0] > result[1]:
            self.swap(result, 0, 1)
        return result

    def swap(self, arr: list[int], idx1: int, idx2: int) -> None:
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

