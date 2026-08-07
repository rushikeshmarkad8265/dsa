class Solution:
	def prevSmaller(self, arr):
		# code here
		n = len(arr)
		ps = [-1]*n
		index = []
		
		for i in range(n):
		    while index and arr[index[-1]] >= arr[i]:
		        index.pop()
		    
		    if not index:
		        ps[i] = -1
		    else:
		        ps[i] = arr[index[-1]]
		    
		    index.append(i)
		    
        return ps