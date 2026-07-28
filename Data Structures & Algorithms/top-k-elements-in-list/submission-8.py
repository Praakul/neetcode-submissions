class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        buckets = [[] for i in range(len(nums)+2)]
        dic = {}

        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0) + 1

        for num, cnt in dic.items():
            buckets[cnt].append(num)
                
        print(buckets)

        for i in range(len(nums)+1, 0, -1):
            if len(buckets[i])==0:
                continue
            for num in buckets[i]:
                ans.append(num)
                k -= 1
                if k==0:
                    return ans
        
        return soll
