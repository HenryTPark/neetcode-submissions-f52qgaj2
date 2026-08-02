class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        iterate through the array backwards
        [30, 38, 30, 36, 35, 40, 28]
          0   1   2   3   4   5   6
         
        []

        if not stack:
            stack.append(0)

        28
        40

        append the len(stack)

        iterate backwords
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stack.pop()
            res[i] = 0 if not stack else stack[-1] - i

            stack.append(i)

        [5]

        res = [0] * n
        '''
        # O(N) Time | O(N) Space
        

        n = len(temperatures)
        stack = []
        result = [0] * n
        
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            result[i] = 0 if not stack else stack[-1] - i

            stack.append(i)

        return result
            




        