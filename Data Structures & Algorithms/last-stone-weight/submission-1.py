import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [x for x in stones]
        heapq.heapify_max(stones_heap)

        while len(stones_heap) > 1:
            first, second = heapq.heappop_max(stones_heap), heapq.heappop_max(stones_heap)
            if first != second:
                remainder = first - second
                heapq.heappush_max(stones_heap, remainder)
    
        return heapq.heappop_max(stones_heap) if len(stones_heap) == 1 else 0