class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def backtrack(i, c):
            if i == len(nums):
                result.add(tuple(sorted(c)))
                return

            c.append(nums[i])
            backtrack(i + 1, c)
            c.pop()

            backtrack(i + 1, c)

        
        backtrack(0, [])

        return [list(tup) for tup in result]
        

        