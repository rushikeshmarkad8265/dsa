class Solution:
    def findAnswer(self, d, n): 
       #Code here
       n = n % 7
       if n < d:
           return d - n
       else:
            return 7+d - n