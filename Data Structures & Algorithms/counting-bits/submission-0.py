class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n + 1):
            num_bits = 0
            temp = num

            while temp:
                temp &= temp - 1
                num_bits += 1

            res.append(num_bits)

        return res
