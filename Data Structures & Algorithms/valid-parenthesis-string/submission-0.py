class Solution:
    def checkValidString(self, s: str) -> bool:
        # O(N) Time | O(N) Space
        open_indices = []
        star_indices = []

        for i, char in enumerate(s):
            if char == '(':
                open_indices.append(i)
            elif char == '*':
                star_indices.append(i)
            else:
                if open_indices:
                    open_indices.pop()
                elif star_indices:
                    star_indices.pop()
                else:
                    return False

        while open_indices and star_indices:
            if open_indices[-1] > star_indices[-1]:
                return False

            open_indices.pop()
            star_indices.pop()

        return len(open_indices) == 0