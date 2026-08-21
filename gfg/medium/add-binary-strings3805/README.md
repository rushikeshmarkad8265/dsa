# Add Binary Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two binary strings **s1**  and  **s2**  consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
 **Note:** The input strings may contain leading zeros but the output string should not have any leading zeros.

```
Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

```

```
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
 100
+ 10
 110

```

 **Constraints:** 
1 ≤s1.size(), s2.size()≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-21T13:30:13.751Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/add-binary-strings3805/1)