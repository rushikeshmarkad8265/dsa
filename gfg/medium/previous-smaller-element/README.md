# Previous Smaller Element

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array  **arr[ ]**.  The task is to find Previous Smaller Element (PSE) for every element in the array. The Previous Smaller Element (PSE) of an element  **x**  is the first element that appears to the left of  **x**  in the array and is strictly smaller than  **x**.

 **Note:**  If no such element exists, assign  **-1**  as the PSE for that position.

 **Examples:** 

```
Input: arr[] = [1, 6, 2]
Output: [-1, 1, 1]
Explanation:
For 1, there is no element on the left, so answer is -1.
For 6, previous smaller element is 1.
For 2, previous smaller element is 1.
```

```
Input: arr[] = [1, 5, 0, 3, 4, 5]
Output: [-1, 1, -1, 0, 3, 4]
Explanation:
For 1, no element on the left, so answer is -1.
For 5, previous smaller element is 1.
For 0, no element on the left smaller than 0, so answer is -1.
For 3, previous smaller element is 0.
For 4, previous smaller element is 3.
For 5, previous smaller element is 4.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T07:05:41.013Z  

```py
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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/previous-smaller-element/1)