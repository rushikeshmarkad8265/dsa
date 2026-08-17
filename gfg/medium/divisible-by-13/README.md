# Divisible by 13

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a number represented as a string  **s**  (which may be very large), check whether it is divisible by 13 or not.

 **Examples:** 

```
Input : s = "2911285"
Output : true
Explanation: 2911285 / 13 = 223945, which is a whole number with no remainder.
```

```
Input : s = "27"
Output : false
Explanation: 27 / 13 ≈ 2.0769..., which is not a whole number (there is a remainder).
```

**Constraints:
**1 ≤  s.size()  ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-17T10:23:49.596Z  

```py
class Solution:
    def divby13(self, s: str) -> int:
        # Step 1: Initialize the running remainder
        remainder = 0
    
        # Step 2: Process each character digit-by-digit
        for char in s:
            # Update the remainder using math: (remainder * 10 + current_digit) % 13
            remainder = (remainder * 10 + int(char)) % 13
    
        # Step 3: Return 1 if perfectly divisible (remainder is 0), otherwise 0
        return 1 if remainder == 0 else 0

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/divisible-by-13/1)