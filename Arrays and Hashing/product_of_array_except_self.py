class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, res = [1]*len(nums), [1]*len(nums), []
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix)
        
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        
        return res