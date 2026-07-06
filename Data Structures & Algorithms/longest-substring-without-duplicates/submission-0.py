class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen: set[str] = set()
        n = len(s)

        for r in range(n):
            current = s[r]

            while current in seen:
                seen.discard(s[l])
                l += 1
            
            seen.add(current)

            longest = max(longest, r - l + 1)
        
        return longest