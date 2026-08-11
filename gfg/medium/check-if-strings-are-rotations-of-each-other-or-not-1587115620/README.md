# Strings Rotations of Each Other

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two strings  **s1** and  **s2**, of equal lengths. The task is to check if  **s2**  is a  **rotated version**  of the string  **s1**.

 **Note:**  A string is a rotation of another if it can be formed by moving characters from the start to the end (or vice versa) without rearranging them.

 **Examples :** 

```
Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: After 2 right rotations, s1 will become equal to s2.

```

```
Input: s1 = "aab", s2 = "aba"
Output: true
Explanation: After 1 left rotation, s1 will become equal to s2.
```

```
Input: s1 = "abcd", s2 = "acbd"
Output: false
Explanation: Strings are not rotations of each other.
```

**Constraints:
**1 ≤ s1.size(), s2.size() ≤ 105
s1, s2 consists of lowercase English alphabets.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-11T05:03:51.757Z  

```py
class Solution:
    def areRotations(self, s1, s2):
        # code here
        return s2 in s1+s1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1)