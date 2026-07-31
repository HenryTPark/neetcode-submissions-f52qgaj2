from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(N) Time | O(M) Space
        # M: len(s1) | N: len(s2)
        if len(s1) > len(s2):
            return False

        counter1 = Counter(s1)

        counter2 = defaultdict(int)
        m, n = len(s1), len(s2)

        for i in range(m):
            counter2[s2[i]] += 1

        left = 0
        
        for right in range(m, n):
            if counter1 == counter2:
                return True

            counter2[s2[left]] -= 1
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            counter2[s2[right]] += 1
            
            left += 1

        return counter1 == counter2
            

        