import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [x for x in stones]
        heapq.heapify_max(stones_heap)

        while len(stones_heap) > 0:
            if len(stones_heap) == 1:
                break
            first, second = heapq.heappop_max(stones_heap), heapq.heappop_max(stones_heap)
            if first != second:
                remainder = first - second
                heapq.heappush_max(stones_heap, remainder)
        
        if len(stones_heap) == 1:
            return heapq.heappop_max(stones_heap)
        return 0