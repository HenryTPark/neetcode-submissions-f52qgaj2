class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        half_size = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = half_size - cut1

            left1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            right1 = nums1[cut1] if cut1 < m else float('inf')
            left2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right2 = nums2[cut2] if cut2 < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return max(left1, left2)
                
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = cut1 - 1
            else:
                left = cut1 + 1
            


        