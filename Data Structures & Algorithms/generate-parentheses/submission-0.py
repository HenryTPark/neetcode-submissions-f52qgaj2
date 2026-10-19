class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def backtrack(open, closed):
            if len(current) == n * 2:
                result.append(''.join(current))
                return

            if open:
                current.append('(')
                backtrack(open - 1, closed)
                current.pop()
            
            if closed > open:
                current.append(')')
                backtrack(open, closed - 1)
                current.pop()

        backtrack(n, n)

        return result

        

        
        