# Factorials of large numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer  **n,**  find its factorial. Return a list of integers denoting the digits that make up the factorial of n.

 **Examples:** 

```
Input: n = 5
Output: [1, 2, 0]
Explanation: 5! = 1 *2* 3 *4* 5 = 120

```

```
Input: n = 10
Output: [3, 6, 2, 8, 8, 0, 0]
Explanation: 10! = 1 *2* 3 *4* 5 *6* 7 *8* 9*10 = 3628800

```

```
Input: n = 1
Output: [1]
Explanation: 1! = 1 
```

 **Constraints** :
1 ≤ n ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-21T12:42:04.779Z  

```py
class Solution:
    def factorial(self, n):
        #code here
        ans = 1
        for i in range(1,n+1):
            ans*=i
        
        ans = str(ans)
        return list(ans)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1)