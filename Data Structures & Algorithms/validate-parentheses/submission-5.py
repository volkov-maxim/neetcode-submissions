from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        close_open = {"]": "[", ")": "(", "}": "{"}
        seen = deque()
        for char in s:
            if seen and char in close_open:
                if close_open[char] != seen.pop():
                    return False
            else:
                seen.append(char)
        return not seen