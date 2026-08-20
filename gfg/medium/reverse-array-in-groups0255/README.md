# Reverse Array in Groups

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]** and an integer  **k**, reverse every consecutive group of k elements. If fewer than k elements remain at the end, reverse all of them.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.
```

```
Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]
Explnation: Since k is greater than the number of remaining elements, the entire array is reversed.
```

 **Constraints:** 
1 ≤ arr.size(), k ≤ 105
1 ≤ arr[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T06:38:40.228Z  

```py
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
            
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1)