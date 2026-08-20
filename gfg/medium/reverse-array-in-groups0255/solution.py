class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        if k>len(arr):
            
            return arr.reverse()
        
        is_need = False
        start = 0
        for i in range(0,len(arr),k):
            start = i
            end = i+k-1
            if end>=len(arr):
                is_need = True
                break
            
            while(start<=end):
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
            
        if is_need:
            end = len(arr)-1
            while(start<=end):
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        
        return arr
            