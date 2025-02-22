class Solution:
    def reverse(self, x: int) -> int:
        max= 2**31-1
        min= -2**31
        sign=1
        reverse=0
        if x<0:
            sign=-1
            x*=-1
        while x>0:
            digit= x%10
            x=x//10
            reverse= reverse*10+digit
        reverse*=sign
        if reverse>max or reverse<min:
            return 0
        return reverse



        