class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def backtrack(index, current):
            if index == len(digits):
                result.append(''.join(current))
                return

            for char in letters[int(digits[index])]:
                current.append(char)
                backtrack(index + 1, current)
                current.pop()

        backtrack(0, [])

        return result
        