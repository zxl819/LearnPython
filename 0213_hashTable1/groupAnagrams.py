class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def isAnagram(s: str, t: str) -> bool:
            from collections import defaultdict
            s_counter = defaultdict(int)
            t_counter = defaultdict(int)

            for S in s:
                s_counter[S] += 1
            for T in t:
                t_counter[T] += 1
            return s_counter == t_counter
        
        ans = []  # 用于存储最终的分组列表
        checked = [False] * len(strs)  # 标记数组，用于记录字符串是否已经被分组

        for i in range(len(strs)):
            if not checked[i]:
                # 对于每个未被检查的字符串，创建一个新组，并标记为已检查
                group = [strs[i]]
                checked[i] = True
                for j in range(i + 1, len(strs)):
                    if not checked[j] and isAnagram(strs[i], strs[j]):
                        # 如果找到异位词且未被检查，添加到当前组，并标记为已检查
                        group.append(strs[j])
                        checked[j] = True
                # 将当前组添加到答案列表中
                ans.append(group)
                
        return ans
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
            
