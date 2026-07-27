# Peak element

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array  **arr[]** where no two adjacent elements are same, find the  **index** of a  **peak** element. An element is considered to be a  **peak**  if it is greater than its adjacent elements (if they exist).

If there are multiple peak elements, Return index of any one of them. The output will be  **"true"**  if the index returned by your function is correct; otherwise, it will be " **false"**.

 **Note:**  Consider the element  **before** the  **first** element and the element  **after** the  **last** element to be  **negative infinity**.

**Examples :
**

```
Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
```

```
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.
```

 **Constraints:** 
1 ≤ arr.size() ≤ 106
-231 ≤ arr[i] ≤ 231 - 1

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T17:47:59.526Z  

```py
class Solution:   
    def peakElement(self, arr):
        # Code here
        if len(arr)==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[len(arr)-1]>arr[len(arr)-2]:
            return len(arr)-1
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i
        
        return 0
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/peak-element/1)