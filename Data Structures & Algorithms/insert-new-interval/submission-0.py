class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        merged_intervals: list[list[int]] = []
        n = len(intervals)
        i = 0

        while i < n and self.comes_before(intervals[i], new_interval):
            merged_intervals.append(intervals[i])
            i += 1
        
        if len(merged_intervals) == 0:
            merged_intervals.append(new_interval)
        elif self.is_overlapping(merged_intervals[-1], new_interval):
            merged_intervals[-1] = self.merge_intervals(merged_intervals[-1], new_interval)
        else:
            merged_intervals.append(new_interval)
        
        while i < n:
            if self.is_overlapping(merged_intervals[-1], intervals[i]):
                merged_intervals[-1] = self.merge_intervals(merged_intervals[-1], intervals[i])
            else:
                merged_intervals.append(intervals[i])
            i += 1
        
        return merged_intervals

    def merge_intervals(self, intv1: list[int], intv2: list[int]) -> list[int]:
        return [min(intv1[0], intv2[0]), max(intv1[-1], intv2[-1])]
    
    def comes_before(self, intv1: list[int], intv2: list[int]) -> bool:
        return intv1[0] <= intv2[0]
    
    def is_overlapping(self, intv1: list[int], intv2: list[int]) -> bool:
        return intv1[-1] >= intv2[0]
        