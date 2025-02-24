class Solution:
    def romanToInt(self, s: str) -> int:
        val= {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot=0
        prev=0
        for char in reversed(s):
            curr= val[char]
            if curr<prev:
                tot-=curr
            else:
                tot+=curr
            prev=curr
        return tot
        