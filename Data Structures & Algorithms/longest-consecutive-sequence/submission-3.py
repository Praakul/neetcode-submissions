class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        leng = 1
        max_len = 1

        if len(nums) == 0:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        for index,num in enumerate(nums):
            if index == (len(nums) - 1):
                break
            else:
                if num + 1 == nums[index+1]:
                    leng += 1
                    if leng > max_len:
                        max_len = leng
                else:
                    leng = 1
        return max_len
        