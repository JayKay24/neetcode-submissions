class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: dict[tuple[int, ...], list[str]] = {}

        for s in strs:
            counter = [0] * 26
            for char in s:
                counter_idx = ord(char) - ord('a')
                counter[counter_idx] += 1
            counter_tuple = tuple(counter)
            if counter_tuple in result:
                result[counter_tuple].append(s)
            else:
                result[counter_tuple] = [s]
        
        return list(result.values())