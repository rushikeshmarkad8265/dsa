class Solution:
    def floorSqrt(self, n): 
        # code here
        start = 0
        end = n
        while(start <= end):
            mid = (start+end)//2
            if mid*mid > n:
                end = mid -1
            else:
                start = mid+1
        
        return start-1