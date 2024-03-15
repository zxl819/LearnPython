class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        if fruits == [0]:
            return 1
        l = 0

        blanket = [fruits[0], fruits[1]]
        subArray = []
        max_len = 0
        for r in range(len(fruits) - 1):
            blanket[0],blanket[1] = fruits[r], fruits[r+1]
            # subArray.append(fruits[r])
            while (l < len(fruits)):
                if(fruits[l] in blanket):
                    subArray.append(fruits[l])
                    l += 1
                    max_len = max(max_len,len(subArray))
                else:
                    subArray = []
                    l = r + 1
                    break
        return max_len


fruits = [0,1,2,2]
Solution().totalFruit(fruits)

for x in fruits:
    print(x)