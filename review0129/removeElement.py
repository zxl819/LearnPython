class Solution:
    def removeElement(self,nums:list[int],val:int):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                i +=1
                nums[i] = nums[j]
        
        return i
    
nums = [3,2,2,3]
val = 3

print(Solution().removeElement(nums,val))
