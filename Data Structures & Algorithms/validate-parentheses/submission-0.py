class Solution:
    def isValid(self, s: str) -> bool:
        # O(N) Time | O(N) Space
        stack = []
        close_to_open = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for char in s:
            if char not in close_to_open:
                stack.append(char)
            else:
                if not stack or stack.pop() != close_to_open[char]:
                    return False

        return len(stack) == 0
        