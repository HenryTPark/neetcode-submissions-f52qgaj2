class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []


        def dfs(start_idx):
            if start_idx == len(s):
                result.append(path[:])
                return

            for end_idx in range(start_idx, len(s)):
                substring = s[start_idx : end_idx + 1]

                if substring == substring[::-1]:
                    path.append(substring)
                    dfs(end_idx + 1)
                    path.pop()

        dfs(0)

        return result
        

        
        