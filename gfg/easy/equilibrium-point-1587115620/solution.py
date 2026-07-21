class Solution:
    def findEquilibrium(self, arr):
        # code here
        
        n = len(arr)
        total_sum = 0
        # ans = -1
        for i in range(n):
            total_sum+=arr[i]
        
        left_sum = 0
        right_sum = total_sum-arr[0]
        for i in range(1,n-1):
            left_sum+=arr[i-1]
            right_sum = right_sum-arr[i]
            
            if left_sum == right_sum:
                return i
        
        return -1
