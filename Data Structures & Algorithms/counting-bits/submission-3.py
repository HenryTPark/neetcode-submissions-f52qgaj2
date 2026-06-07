class Solution:
    def countBits(self, n: int) -> List[int]:
        def hamming_weight(num):
            res = 0

            while num:
                num &= (num - 1)
                res += 1

            return res

        res = []

        for i in range(n + 1):
            res.append(hamming_weight(i))

        return res

        