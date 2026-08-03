# Length of the Longest Alphabetical Continuous Substring

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

An  **alphabetical continuous string**  is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string `"abcdefghijklmnopqrstuvwxyz"`.

- For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.

Given a string `s` consisting of lowercase letters only, return the  *length of the  **longest**  alphabetical continuous substring.* 

 

 **Example 1:** 

```
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.

```

 **Example 2:** 

```
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.

```

 

 **Constraints:** 

- 1 <= s.length <= 105
- s consists of only English lowercase letters.

## Solution

**Language:** Python  
**Runtime:** 196 ms (beats 18.46%)  
**Memory:** 19.9 MB (beats 95.13%)  
**Submitted:** 2026-08-03T04:18:36.285Z  

```py
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = ''
        temp = s[0]
        for i in range(len(s)-1):           
            if ord(s[i])==ord(s[i+1])-1:
                temp+=s[i+1]
            
            else :
                if len(ans)<len(temp):
                    ans=temp
                temp = s[i+1]
        if len(ans)<len(temp):
             ans=temp

        return len(ans)
```

---

[View on LeetCode](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/)