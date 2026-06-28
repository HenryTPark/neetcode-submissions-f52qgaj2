from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(N) Time | O(N) Space
        counter = Counter(nums)
        freq_map = defaultdict(list)

        for num, count in counter.items():
            freq_map[count].append(num)

        result = []

        for freq in range(len(nums), -1, -1):
            for num in freq_map[freq]:
                result.append(num)

                k -= 1

                if k == 0:
                    return result

        

        
        