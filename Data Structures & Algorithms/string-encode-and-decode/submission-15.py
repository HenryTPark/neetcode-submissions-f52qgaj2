class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            length = len(word)

            res.append(str(length) + '#' + word)

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        res = []

        while i < n:
            j = i
            
            while j < n and s[j] != '#':
                j += 1
            
            print(f'(i, j): {(i, j)}')
            
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            
            i = j+1+length

        return res
