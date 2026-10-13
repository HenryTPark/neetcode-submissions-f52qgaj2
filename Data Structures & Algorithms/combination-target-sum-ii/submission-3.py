class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        n = len(candidates)

        def backtrack(start, current, total):
            if total == target:
                result.append(list(current))
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result
