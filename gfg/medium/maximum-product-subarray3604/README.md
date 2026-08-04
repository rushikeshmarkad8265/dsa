# Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  that contains positive and negative integers (may contain 0 as well). Find the  **maximum**  product that we can get in a subarray of  **arr[]**.

 **Note:**  It is guaranteed that the answer fits in a 32-bit integer.

**Examples
**

```
Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6  *(-3)*  (-10) = 180.
```

```
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.
```

```
Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
```

 **Constraints:** 
1 ≤ arr.size() ≤ 106
-100 ≤ arr[i] ≤ 100

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T18:56:29.615Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1)