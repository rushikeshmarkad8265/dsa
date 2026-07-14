# Zigzag Conversion

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R

```

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string s, int numRows);

```

 

 **Example 1:** 

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

```

 **Example 2:** 

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

```

 **Example 3:** 

```
Input: s = "A", numRows = 1
Output: "A"

```

 

 **Constraints:** 

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 59.98%)  
**Memory:** 19.4 MB (beats 47.70%)  
**Submitted:** 2026-07-14T09:46:01.374Z  

```py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        d = 1
        i = 0
        rows = [[] for _ in range(numRows)]
        for ch in s:
            rows[i].append(ch)
            if i == 0:
                d = 1
            elif i == numRows-1:
                d = -1
            i = i+d
        
        result = ''
        for i in range(numRows):
            result += ''.join(rows[i])


        return result

```

---

[View on LeetCode](https://leetcode.com/problems/zigzag-conversion/)