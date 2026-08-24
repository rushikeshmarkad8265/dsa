# print-alternate-elements-of-an-array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-24T19:40:26.178Z  

```py
class Solution:
    def getAlternates(self, arr):
        # Code Here
        ans = []
        for i in range(0,len(arr),2):
            ans.append(arr[i])
            
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1)