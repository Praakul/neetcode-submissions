class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = {nums[i] : i for i in range(len(nums))}

        print(nums_dic)

        for index, num in enumerate(nums):
            ans = nums_dic.get(target - num)
            if not ans is None and ans != index:
                return [index,ans]