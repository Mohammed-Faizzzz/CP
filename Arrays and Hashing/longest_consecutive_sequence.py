class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store all in hashmap, then iterate through --> 2(n)
        # check if key - 1 in hashmap --> if not, it is the start of the seq
        # then keep gg and finding key + 1, and add that

        if len(nums) <= 1:
            return len(nums)

        visited = set()
        for num in nums:
            visited.add(num)
        
        longest = 1

        for key in visited:
            curr = 1
            if key - 1 not in visited: # start of seq
                while key + 1 in visited:
                    curr += 1
                    key += 1
                longest = max(longest, curr)
        
        return longest
        