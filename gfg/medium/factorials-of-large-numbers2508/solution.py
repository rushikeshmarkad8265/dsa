class Solution:
    def factorial(self, n):
        #code here
        ans = 1
        for i in range(1,n+1):
            ans*=i
        
        ans = str(ans)
        return list(ans)