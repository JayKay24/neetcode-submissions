class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        pairs = {")": "(", "}": "{", "]": "["}
        stack: list[str] = []

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif len(stack) == 0 or stack.pop() != pairs[char]:
                return False
        
        return len(stack) == 0