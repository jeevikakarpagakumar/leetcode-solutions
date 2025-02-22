class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        sign=1
        result=0
        int_max= 2**31-1
        int_min= -2**31
        while i<len(s) and s[i]==' ':
            i+=1
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            sign=1 if s[i]=='+' else -1
            i+=1
        while i<len(s) and s[i].isdigit():
            digit= int(s[i])
            if result>(int_max-digit)//10:
                return int_min if sign==-1 else int_max
            result= result*10+digit
            i+=1

        return sign*result