class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        running_interval = intervals[0]
        n = len(intervals)

        for i in range(1, n):
            current_interval = intervals[i]
            if self.is_overlapping(running_interval, current_interval):
                running_interval = self.get_merged_intervals(running_interval, current_interval)
            else:
                result.append(running_interval)
                running_interval = current_interval
        
        result.append(running_interval)

        return result

    
    def is_overlapping(self, interval_1: list[int], interval_2: list[int]) -> bool:
        return interval_1[1] >= interval_2[0]
    
    def get_merged_intervals(self, interval_1: list[int], interval_2: list[int]) -> list[int]:
        new_interval = [0, 0]
        
        new_interval[0] = min(interval_1[0], interval_2[0])
        new_interval[1] = max(interval_1[1], interval_2[1])

        return new_interval

        