class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        # buckets = [[] * (n + 1)]
        counter = Counter(nums)

        for num, freq in counter.items():
            buckets[freq].append(num)

        result = []

        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
        
        