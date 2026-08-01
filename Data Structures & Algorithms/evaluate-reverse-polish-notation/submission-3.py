class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(N) Time | O(1) Space
        stack = []

        for token in tokens:
            if token == '+':
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val1 + val2)
            elif token == '-':
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val2 - val1)
            elif token == '*':
                val1, val2 = stack.pop(), stack.pop()
                stack.append(val1 * val2)
            elif token == '/':
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        
        return stack[-1]


        