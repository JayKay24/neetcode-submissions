class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        num = 0
        current = []
        stack: list[tuple[str, int]] = []

        for i in range(n):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append(("".join(current), num))
                num = 0
                current = []
            elif char == "]":
                prev, k = stack.pop()
                current = list(prev) + current * k
            else:
                current.append(char)

        return "".join(current)