class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        
        for num in nums:
            if num - 1 not in numSet:
                temp = num
                length = 0
                
                while temp in numSet:
                    temp += 1
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
        # if not nums:
        #     return 0
        # nums.sort()
        # seriesCounter = {}
        # for num in nums:
        #     if num - 1 in seriesCounter:
        #         seriesCounter[num] = seriesCounter[num - 1] + 1
        #     else:
        #         seriesCounter[num] = 1
        # return max(seriesCounter.values())

            