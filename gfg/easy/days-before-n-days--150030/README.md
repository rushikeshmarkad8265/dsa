# Day before N days

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers  **d**  and  **n.** Where  **d**  is the day, out of 7 days of the week,  **d**  varies from 0 to 6 as shown below.
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday

You have to  **return**  the index for the day which is  **n**  days before the given day  **d.** 

 **Examples:** 

```
Input: d = 4, n = 3
Output: 1
Explanation: 3 days before the 4th(Thursday) is 1(Monday).
```

```
Input: d = 2, n = 19
Output: 4
Explanation: 19 days before the 2nd(Tuesday) is 4(Thursday).

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-08T11:08:20.764Z  

```py
class Solution:
    def findAnswer(self, d, n): 
       #Code here
       n = n % 7
       if n < d:
           return d - n
       else:
            return 7+d - n
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/days-before-n-days--150030/1)