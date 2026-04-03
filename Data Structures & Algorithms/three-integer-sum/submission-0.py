class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(N^2) Time | O(1) Aux Space | O(N) Total Space
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return res
        
        
        