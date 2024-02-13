class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import defaultdict
        needMap = defaultdict(int)
        checkMap = defaultdict(int)
        res = []
        for P in p:
            needMap[P] += 1
        
        for i in range(len(s)):
            if i + len(p) <= len(s):
                for j in range(i, i + len(p)):
                    checkMap[s[j]] += 1
                if needMap == checkMap:
                    res.append(i)
                checkMap = defaultdict(int)
        return res
    
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
    
    # 初始化字符计数器
        p_count, s_count = defaultdict(int), defaultdict(int)
        for c in p:
            p_count[c] += 1
    
        result = []
        left = 0  # 窗口左边界
        for right in range(len(s)):  # right是窗口右边界
            s_count[s[right]] += 1  # 将当前字符加入到s的计数器
        
        # 如果窗口大小等于p的长度
            if right - left + 1 == len(p):
                if s_count == p_count:
                    result.append(left)  # 找到一个异位词的起始索引
                s_count[s[left]] -= 1  # 移除窗口最左边的字符计数
                if s_count[s[left]] == 0:
                    del s_count[s[left]]  # 如果字符数量为0，从计数器中删除该字符
                left += 1  # 窗口左移
    
        return result

s = "abab"
p = "ab"
print(Solution().findAnagrams(s, p))

