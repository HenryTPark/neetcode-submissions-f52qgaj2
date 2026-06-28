class Solution:
    def encode(self, strs: List[str]) -> str:
        result = []

        for word in strs:
            result.append(f'{len(word)}#{word}')

        return ''.join(result)
        


    def decode(self, s: str) -> List[str]:

        print(s)
        i = 0
        result = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            result.append(s[j + 1 : j + length + 1])

            i = j + length + 1

        return result
