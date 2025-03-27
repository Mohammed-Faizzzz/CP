class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) + 1)]
        if len(nums) == 1:
            freq.append([])
        nums = sorted(nums)
        prev = nums[0]
        cnt = 0
        for num in nums:
            if num != prev:
                freq[cnt].append(prev)
                cnt = 0
                prev = num
            cnt += 1
        freq[cnt].append(prev)

        res = []
        length_res = 0
        print(freq)
        for idx in freq[::-1]:
            print(idx, res)
            if len(idx) != 0 and length_res < k:
                res.extend(idx)
                length_res += len(idx)
        return res
        