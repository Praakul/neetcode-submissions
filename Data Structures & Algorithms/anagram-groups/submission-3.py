class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dic = {}
        output = []
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if not key in str_dic.keys():
                str_dic[key] = [strs[i]]
            else:
                str_dic[key].append(strs[i])

        output = [value for value in str_dic.values()]
        return output