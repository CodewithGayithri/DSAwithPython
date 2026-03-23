class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            a = ord(s[i])
            b = ord(s[i+1])
            ans = abs(a - b)
            sum = sum + ans
        return sum
c= Solution()
print(c.scoreOfString("hello"))