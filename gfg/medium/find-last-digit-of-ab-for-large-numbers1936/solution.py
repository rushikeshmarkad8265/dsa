class Solution:
    def getLastDigit(self, a, b):
        # code here
        a = int(a)
        b = int(b)
        if a == 0 and b == 0:
            return 1
        return pow(a,b,10)