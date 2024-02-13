class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        for S in s:
            s_counter[S] += 1
        for T in t:
            t_counter[T] += 1
        return s_counter == t_counter