class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        print(s)
        leng = len(s)
        for i in range(leng):
            print(f's[i]:{s[i]}, s[leng - 1 -i]:{s[leng -1 - i]}')
            if not s[i] == s[leng -1 - i]:
                return False 
        return True
        