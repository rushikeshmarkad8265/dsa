# Nth Number without Digit 9

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a positive integer  **n** as string. Find  **nth**  natural number after removing all the numbers containing the digit  **9** and return it as string.

 **Examples :** 

```
Input: n = "8"
Output: "8"
Explanation: After removing natural numbers which contains digit 9, first 8 numbers are 1,2,3,4,5,6,7,8 and 8th number is 8.
```

```
Input: n = "9"
Output: "10"
Explanation: After removing natural numbers which contains digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10 and 9th number is 10.

```

 **Constraints:** 
1 ≤ n.length() ≤ 20

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-17T10:05:12.551Z  

```py
class Solution:
    def findNth(self, n: int) -> str:
        # Step 1: Handle string inputs if necessary
        n = int(n)
    
        # Step 2: Convert base-10 integer n into a base-9 string
        result = []
        while n > 0:
            remainder = n % 9
            result.append(str(remainder))
            n = n // 9
    
        # Step 3: Reverse the list and join to form the final number string
        return "".join(reversed(result))

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/nth-natural-number/1)