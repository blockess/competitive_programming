class Solution:
    def titleToNumber(self, s):
        return sum([26**i * (ord(c.upper()) - 64) for i,c in enumerate(s[::-1])])
