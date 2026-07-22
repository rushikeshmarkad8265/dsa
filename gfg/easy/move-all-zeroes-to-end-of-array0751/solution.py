class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	n = len(arr)
    	start = 0
    	end = n-1
    	zero = 0
        
        while(start < n):
            if arr[start]!=0:
                arr[start],arr[zero] =arr[zero],arr[start]
                start+=1
                zero+=1
            
            else:
                start+=1
                
                