# Q1. Count Valid Prefixes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **binary**  string `s`.

A  **prefix**  of `s` is considered  **valid**  if its characters can be rearranged to form an  **alternating**  string.

Return the number of valid prefixes of `s`.

A  **binary**  string is a string consisting only of `'0'` and `'1'`.

A  **prefix**  of a string is a  **substring**  that starts from the beginning of the string and extends to any point within it.

A  **substring**  is a contiguous  **non-empty**  sequence of characters within a string.

A string is considered  **alternating**  if no two adjacent characters are equal.

 

 **Example 1:** 

 **Input:**  s = "00101"

 **Output:**  3

 **Explanation:** 

The valid prefixes are:

- "0": It is already an alternating string.
- "001": It can be rearranged into "010", which is an alternating string.
- "00101": It can be rearranged into "01010", which is an alternating string.

Thus, the answer is 3.

 **Example 2:** 

 **Input:**  s = "101"

 **Output:**  3

 **Explanation:** 

All prefixes of `s = "101"` are already alternating strings. Thus, the answer is 3.

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists only of '0' and '1'.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 21.25%)  
**Memory:** 19.2 MB (beats 75.57%)  
**Submitted:** 2026-08-01T16:35:28.789Z  

```py
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        n = len(s)
        freq_map = {'0':0,'1':0}
        ans = 0
        for ch in s:
            freq_map[ch] = freq_map.get(ch)+1
            if freq_map['0']==freq_map['1']+1 or freq_map['1'] == freq_map['0']+1 or freq_map['0']==freq_map['1']:
                ans+=1
        return ans
            
```

---

[View on LeetCode](https://leetcode.com/problems/count-valid-prefixes/)