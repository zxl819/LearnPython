class Solution:
    def longestCommonPrefix(self,strs:list[str]):
        if not strs:
            return ""
        
        strs.sort()
        
        first_str = strs[0]
        last_str = strs[-1]
        max_length = []

        for i in range(min(map(len,strs))):# 不能这个范围range(len(strs))
            if first_str[i] == last_str[i]:
                max_length.append(first_str[i])
            else:
                break
        return "".join(max_length)

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))