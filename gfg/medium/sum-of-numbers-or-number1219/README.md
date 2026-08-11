# Sum Two Large Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings denoting non-negative numbers s1 and s2. Calculate the sum of s1 and s2.

 **Examples:** 

```
Input: s1 = "25", s2 = "23"
Output: "48"
Explanation: The sum of 25 and 23 is 48.
```

```
Input: s1 = "2500", s2 = "23"
Output: "2523"
Explanation: The sum of 2500 and 23 is 2523.
```

```
Input: s1 = "2", s2 = "3"
Output: "5"
Explanation: The sum of 2 and 3 is 5.
```

 **Constraints:** 
1 <= |s1|, |s2| <= 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-11T05:15:08.562Z  

```py
class Solution:
    def findSum(self, s1, s2):

        i = len(s1) - 1
        j = len(s2) - 1

        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:

            a = int(s1[i]) if i >= 0 else 0
            b = int(s2[j]) if j >= 0 else 0

            total = a + b + carry

            ans.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        result = ''.join(reversed(ans))

        # Remove leading zeros
        result = result.lstrip('0')

        # If everything was zero
        return result if result else "0"
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-numbers-or-number1219/1)