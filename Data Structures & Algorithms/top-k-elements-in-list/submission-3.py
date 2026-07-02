class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        counter = {}
        sorter = [[] for i in range(len(nums)+1)]    

        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i],0)

        sol = []

        for key, value in counter.items():
            sorter[value].append(key)

        for i in range(len(sorter) - 1, 0, -1):
            for j in range(len(sorter[i])):
                sol.append(sorter[i][j])
                if len(sol) == k:
                    return sol