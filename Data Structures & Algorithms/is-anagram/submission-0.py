class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = self.get_freq_count(s)

        for char in t:
            if char not in s_freq:
                return False
            s_freq[char] -= 1
            if s_freq[char] == 0:
                del s_freq[char]
        
        return len(s_freq) == 0

    def get_freq_count(self, s: str) -> dict[str, int]:
        s_freq: dict[str, int] = {}

        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        return s_freq