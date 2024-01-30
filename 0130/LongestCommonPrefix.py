class Solution:
    def LongestPalindrome(self,strs:list[str]):
        if not strs:
            return ""
        
        strs.sort()
        first_str =strs[0]
        last_str = strs[-1]
        common_prefix = []

        for i in range(min(map(len,strs))):
            if first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            
        return "".join(common_prefix)        
    
strs = ["dog","racecar","car"]
print(Solution().LongestPalindrome(strs))

            

    