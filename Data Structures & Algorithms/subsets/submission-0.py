class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]


        for num in nums:
            l = len(result)

            for i in range(l):
                result.append(result[i] + [num])
            
        
        return result

            



        
        