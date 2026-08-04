class Solution:
    def numberOfSquares(self, base):
        # Code here
        ans = base -2
        ans = ans // 2
        ans = (ans * (ans+1))//2
        return ans