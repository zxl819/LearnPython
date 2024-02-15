class Solution:
    def repeatedSubstringPattern(self, s: str):
        from collections import defaultdict
        classMap = defaultdict(int)
        class0 = []
        if len(s)%2 != 0:
            return False
        for S in s:
            if classMap[S] >= 1:
                break
            class0.append(S)
            classMap[S] += 1

        if 2 * len(class0) > len(s):
             return False
        # ans = len(s) - len(class0)
        for i in range(len(s) - len(class0)):
            j = i + len(class0)
            k = i % len(class0)
            if s[j] == class0[k]:
                continue
            else:
                return False
        return True

def repeated_substring_pattern(s: str) -> bool:
    # 检查字符串s是否可以通过它的一个子串重复多次构成
    # 方法是将原字符串s复制一遍拼接，然后去掉首尾各一个字符，如果s仍然在新字符串中，则说明可以
    return s in (s + s)[1:-1]
s = "abcabcabcabc"
print(repeated_substring_pattern(s))
print(Solution().repeatedSubstringPattern(s))
            

