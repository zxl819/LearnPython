class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        res = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                seq_len = 1
                while (num + 1) in num_set:
                    seq_len += 1
                    num += 1
                res = max(res, seq_len)
        return res

            