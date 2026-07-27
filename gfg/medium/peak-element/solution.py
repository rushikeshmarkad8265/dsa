class Solution:   
    def peakElement(self, arr):
        # Code here
        if len(arr)==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[len(arr)-1]>arr[len(arr)-2]:
            return len(arr)-1
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i
        
        return 0