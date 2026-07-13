import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter: dict[int, int] = self.get_frequency_count(nums)
        pq = []
        
        for k_item, v in freq_counter.items():
            heapq.heappush(pq, (v, k_item))
            while len(pq) > k:
                heapq.heappop(pq)
        
        return [item[1] for item in pq]
    
    def get_frequency_count(self, nums: list[int]) -> dict[int, int]:
        freq_counter = {}
        
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1
        
        return freq_counter
        