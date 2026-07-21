class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = []
        '''access each element and then add a delimeter # or something else and then also add length of the word at the back of it'''
        for word in strs:
            new_strs.append(str(len(word))+'#'+word)
        encoded_str = ''.join(new_strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i, j = 0, 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            length = int(s[i:j])

            start = j + 1
            end = start + length

            ans.append(s[start:end])
            i = end

        return ans
            
         