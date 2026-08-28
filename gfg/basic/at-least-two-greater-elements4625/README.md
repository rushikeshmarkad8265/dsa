# At least Two Greater

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array arr of distinct elements, the task is to return an array of all elements except the two greatest elements in sorted order.

 **Examples:** 

```
Input: arr[] = [2, 8, 7, 1, 5]
Output: [1, 2, 5] 
Explanation: Here we return an array contains 1, 2, 5 and we leave two greatest elements 7 & 8. 
```

```
Input: arr[] = [7, -2, 3, 4, 9, -1]
Output: [-2, -1, 3, 4]
Explanation:  Here we return an array contains -2,  -1,  3,  4 and we leave two greatest elements 7 & 9. 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T03:05:23.462Z  

```py
class Solution:
    def findElements(self,arr):
        # code here
        arr.sort()
        return arr[:len(arr)-2]

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/at-least-two-greater-elements4625/1)