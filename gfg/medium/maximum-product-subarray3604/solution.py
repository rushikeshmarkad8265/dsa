class Solution:
	def maxProduct(self,arr):
		# code here
		max_prod = float('-inf')
		product = 1
		prefix = 1
		suffix = 1
		for i in range(len(arr)):
		    if prefix == 0:
		        prefix = 1
		       
		    if suffix == 0:
		        suffix = 1
		    
		    prefix = prefix * arr[i]
		    suffix = suffix * arr[len(arr)-i-1]
		    max_prod = max(max_prod,max(prefix,suffix))
		    
	    
	    return max_prod