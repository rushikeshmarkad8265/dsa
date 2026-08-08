class Solution:
	def find_fact(self, n):
		# Code here
		def fact(n):
		    if n == 1:
		        return 1
		    return n*fact(n-1)
		    
	    return fact(n)