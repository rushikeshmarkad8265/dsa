# Find nth root of m

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given 2 numbers  **n and m,**  the task is to find  **n√m**  (nth root of m). If the root is not integer then return  **-1**.

 **Examples :** 

```
Input: n = 3, m = 8
Output: 2
Explanation: 23 = 8

```

```
Input: n = 3, m = 9
Output: -1
Explanation: 3rd root of 9 is not integer.
```

```
Input: n = 4, m = 16
Output: 2
Explanation: 24 = 16
```

 **Constraints:** 
1 ≤ n ≤ 9
0 ≤ m ≤ 20

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-08T18:45:42.564Z  

```py
class Solution:
    def nthRoot(self, n, m):
       # code here
       m = m ** (1/n)
       if m % 1 == 0:
            return int(m)
       else:
            return -1
        

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1)