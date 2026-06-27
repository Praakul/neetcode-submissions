import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        solution = []
        verification = [False] * len(strs)

        for i in range(len(strs)): 
            sorted_strs.append(sorted(strs[i])) #strs=["act","pots","tops","cat","stop","hat"]
            
        for i in range(len(strs)):
            temp_list = [strs[i]]
            if not verification[i]:
                for j in range(i+1, len(sorted_strs)):
                    if  sorted_strs[i] == sorted_strs[j]:
                        temp_list.append(strs[j])
                        verification[j] = True
                solution.append(temp_list)
                verification[i] = True
        return solution
        
        