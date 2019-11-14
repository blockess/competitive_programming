class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        
        for lp in range(ls,1,-1):
            for si in range(ls-lp+1):
                ei = (lp//2) + si
                sj = ei
                ej = si + lp
                
                if lp % 2:
                    sj += 1
                
                sl = s[si:ei]
                sr = s[sj:ej]
                sr = sr[::-1]
                if sl == sr:
                    return s[si:ej]
        
        if s:
            return s[0]
        else:
            return ""
