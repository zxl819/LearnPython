class Solution:
    def magicTower(self, nums: list[int]):
        if sum(nums) < 0:
            return -1
        
        sorted(nums)
        

nums = [100,100,100,-250,-60,-140,-50,-50,100,150]
print(Solution().magicTower(nums))


            