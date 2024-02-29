class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        tmp = []
        for k in range(len(words)):
            s1 = words[k][:]
            for j in range(len(words[k])):
                if k != len(words[j]):
                    return False
                tmp.append(words[j][k])
            s2 = ''.join(tmp)
            if s1 == s2:
                tmp = []
                continue
            else:
                return False
        if k == len(words) - 1:
            return True
        
    def validWordSquare2(self, words: list[str]) -> bool:
        tmp = []
        for k in range(len(words[0])):
            data = ""
            for j in range(len(words)):
                try:
                    data += words[j][k]
                except:
                    data += ""
            tmp.append(data)
        return words == tmp

words = ["abc","bde","cefg"]
print(Solution().validWordSquare2(words))