class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = []
        pre_pro = []
        post_pro = []

        for i in range(len(nums)):
            if i == 0:
                pre_pro.append(1)
            else:
                pre_pro.append(pre_pro[i-1] * nums[i-1])

        for i in range(len(nums)): # [1,2,4,6] [1,1,2,8]  [1,6,24,48 ]
            if i == 0:
                post_pro.append(1)
            else:
                post_pro.append((nums[len(nums) - i]) * (post_pro[i - 1]))

        for i in range(len(nums)):
            sol.append(pre_pro[i] * post_pro[len(nums) -1 - i])
            
        return sol
        

