class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        ss.sort()
        tt = list(t)
        tt.sort()
        if ss == tt:
            return True
        return False

        