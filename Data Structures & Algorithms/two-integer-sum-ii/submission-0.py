class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(N) Time | O(1) Space
        n = len(numbers)

        left, right = 0, n - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]
        