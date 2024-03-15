class Solution:
    def isMonotonic(nums: list[int]):
        new = sorted(nums)
        print(new)
        print(list(reversed(new)))
        if nums == new :
            return True
        elif nums == list(reversed(new)):
            return True
        else:
            return False
    
nums = [6,5,4,4]
Solution.isMonotonic(nums)