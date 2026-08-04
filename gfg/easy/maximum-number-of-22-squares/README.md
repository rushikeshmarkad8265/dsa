# Squares in Triangle

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the  **base** (in units) of a right-angled isoceles traingle, find the  **maximum**  number of 2X2 squares that can fit in the triangle with given base.

 **Examples:** 

```
Input: base = 8
Output: 6
Explanation:
The bottom row can accommodate 3 squares, the next row 2 squares, and the top row 1 square. Hence, the maximum number of 2 × 2 squares that can fit inside the triangle is: 3 + 2 + 1 = 6.

```

```
Input : base = 7
Output : 3
Explanation : In the base we can keep 2 squares and above the two squares we can only keep 1 square. So the total number of squares are equal to 3.

```

 **Constraints :** 
1 ≤ base ≤ 92682

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T18:40:15.766Z  

```py
class Solution:
    def numberOfSquares(self, base):
        # Code here
        ans = base -2
        ans = ans // 2
        ans = (ans * (ans+1))//2
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-number-of-22-squares/1)