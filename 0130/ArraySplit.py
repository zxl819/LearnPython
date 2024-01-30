class Solution:
    def ArraySplit(self,nums:list[int]):

       return sum(sorted(nums)[::2])
    

nums = [6,2,6,5,1,2]
print(Solution().ArraySplit(nums))
#print(sorted(nums)[::2])