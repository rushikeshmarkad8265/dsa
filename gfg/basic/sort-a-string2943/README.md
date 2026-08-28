# Sort a String

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a string consisting of lowercase letters, arrange all its letters in ascending order. 

 **Examples:** 

```
Input: s = "edcab"
Output: "abcde"
Explanation: characters are in ascending
order in "abcde".

```

```
Input: s = "xzy"
Output: "xyz"
Explanation: characters are in ascending
order in "xyz".
```

 **Constraints:** 
1 ≤ |s| ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-28T03:14:09.997Z  

```py
class Solution:
    def sortString(self, s: str) -> str:
        # code here
        return "".join(sorted(s))
        
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sort-a-string2943/1)