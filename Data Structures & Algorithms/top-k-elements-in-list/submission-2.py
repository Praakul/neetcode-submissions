class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        sol = []
        soll = []

        for i in nums:
            map[i] = 1 + map.get(i, 0)
        
        for num, freq in map.items():
            sol.append([freq,num])
        sol.sort(reverse=True)

        for i in range(k):
            element = sol[i][1]
            soll.append(element)
        
        return soll
