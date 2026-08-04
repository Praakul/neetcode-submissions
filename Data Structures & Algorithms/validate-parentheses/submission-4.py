class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stackk = []
        for i in range(len(s)):
            if s[i] in ('(','[','{'):
                stackk.append(s[i])
            else:
                if len(stackk) == 0:
                    return False
                if s[i] == ')':
                    if not stackk.pop() == '(':
                        return False
                elif s[i] == ']':
                    if not stackk.pop() == '[':
                        return False
                else:
                    if not stackk.pop() == '{':
                        return False
        return len(stackk) == 0



        