class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates that sum to the target.
        Each number can only be used once.
        """
        # O(2^N) Time | O(N) Space
        # N: length of the candidates array

        candidates.sort()
        result = []

        def backtrack(start_idx, current_combo, current_sum):
            # Base case: valid combination found
            if current_sum == target:
                result.append(list(current_combo))
                return

            # Iterate through available candidates starting from start_idx
            for i in range(start_idx, len(candidates)):
                # Skip duplicate elements at the same decision level
                # to avoid duplicate combinations without needing a set()
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue

                # Pruning: Since array is sorted, if current candidate exceeds target,
                # all subsequent candidates will also exceed it
                if current_sum + candidates[i] > target:
                    break

                # Choose
                current_combo.append(candidates[i])
                # Explore (i + 1 because we can't reuse the same element)
                backtrack(i + 1, current_combo, current_sum + candidates[i])
                # Un-choose
                current_combo.pop()

        backtrack(0, [], 0)

        return result