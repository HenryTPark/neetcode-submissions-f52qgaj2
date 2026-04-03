from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_to_nums = [[] for _ in range(len(nums) + 1)]
        
        counter = Counter(nums)

        for num, count in counter.items():
            freq_to_nums[count].append(num)

        res = []
        for count in range(len(nums), -1, -1):
            for num in freq_to_nums[count]:
                res.append(num)
                k -= 1

                if not k:
                    return res

        

        
        