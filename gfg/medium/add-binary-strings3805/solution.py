class Solution:
	def addBinary(self, s1, s2):
		# code here
		i= len(s1)-1
		j = len(s2)-1
		carry = 0
		ans  =""
		while (i>=0 and j>=0):
		    temp = int(s1[i])+int(s2[j])+carry
		    
		    carry = temp//2
		    ans +=str(temp%2)
		    i-=1
		    j-=1
	    
	    if i>-1:
	        while(i>=0):
    		    temp = int(s1[i])+carry
    		    
    		    carry = temp//2
    		    ans +=str(temp%2)
	            i-=1
	   
	    if j > -1:
	        while(j>=0):
    		    temp = int(s2[j])+carry
    		    
    		    carry = temp//2
    		    ans +=str(temp%2)
	   
	            j-=1
        if carry == 1:
            ans+=str(carry)
        
        
	    return ans[::-1].lstrip('0')