class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        atw = defaultdict(list)
        a = ord('a')

        for word in strs:
            counter = [0] * 26

            for char in word:
                code = ord(char)

                counter[code - a] += 1

            atw[tuple(counter)].append(word)

        return list(atw.values())

        