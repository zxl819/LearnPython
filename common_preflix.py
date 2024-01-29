

from typing import Lisclass Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return " "

        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        common_preflix = []

        for i in range(min(len(first_str),len(last_str))):
            if first_str[i] == last_str[i]:
                common_preflix.append(first_str[i])
            else:
                break
        
        return ''.join(common_preflix)tt