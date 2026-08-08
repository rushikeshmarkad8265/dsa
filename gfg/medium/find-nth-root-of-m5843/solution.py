class Solution:
    def nthRoot(self, n, m):
       # code here
       m = m ** (1/n)
       if m % 1 == 0:
            return int(m)
       else:
            return -1
        
