class Solution:
    def rob(self, nums: list[int]) -> int:
        def f(nums):
            prev1=nums[0]
            prev2=0
            for i in range(1,len(nums)):
                take=nums[i]+prev2
                nottake=0+prev1
                total=max(take,nottake)
                prev2=prev1
                prev1=total
            return prev1
        if len(nums)==1:
            return nums[0]
        return max(f(nums[:-1]),f(nums[1:]))
         