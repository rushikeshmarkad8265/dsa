# Longest Substring Without Repeating Characters

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a string `s`, find the length of the  **longest**   **substring**  without duplicate characters.

 

 **Example 1:** 

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

 **Example 2:** 

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

 **Example 3:** 

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

 **Constraints:** 

- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

## Solution

**Language:** Python  
**Runtime:** 187 ms (beats 9.21%)  
**Memory:** 19.3 MB (beats 68.42%)  
**Submitted:** 2026-07-14T09:45:23.772Z  

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        temp = ""
        # length = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)-1):
            temp+=s[i]
            for j in range(i+1,len(s)):
                if s[j] in temp:
                    break
                temp += s[j]         
            ans = max(len(temp),ans)
            temp = ""
        
        return ans

        

```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)