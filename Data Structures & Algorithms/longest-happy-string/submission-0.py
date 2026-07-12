import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush_max(pq, (a, "a"))
        if b > 0:
            heapq.heappush_max(pq, (b, "b"))
        if c > 0:
            heapq.heappush_max(pq, (c, "c"))
        
        result = []

        while pq:
            count, character = heapq.heappop_max(pq)

            if self.is_violating_3_consecutive(character, result):
                if not pq:
                    break
                
                temp_count, temp_char = heapq.heappop_max(pq)
                result.append(temp_char)

                temp_count -= 1
                if temp_count > 0:
                    heapq.heappush_max(pq, (temp_count, temp_char))
                
                heapq.heappush_max(pq, (count, character))
            else:
                result.append(character)
                count -= 1

                if count > 0:
                    heapq.heappush_max(pq, (count, character))
        
        return "".join(result)
    
    def is_violating_3_consecutive(self, character: str, arr: list[str]):
        return len(arr) >= 2 and arr[-1] == character and arr[-2] == character