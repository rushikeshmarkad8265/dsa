# Longest Consecutive Subsequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  of non-negative integers. Find the  **length**  of the longest sub-sequence such that elements in the subsequence are consecutive integers, the **consecutive numbers**  can be in  **any order.** 

 **Examples:** 

```
Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.
```

```
Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.
```

```
Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.

```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-22T13:25:34.705Z  

```py
class Solution:
    def longestConsecutive(self, arr):
        # code here
        st = set()
        n = len(arr)
        
        for val in arr:
            st.add(val)
        count = 0
        ans = float("-inf")
        for val in st:
            if val-1 not in st:
                temp = val
                while temp in st:
                    count+=1
                    temp+=1
                ans = max(ans,count)
                count = 0
        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1)