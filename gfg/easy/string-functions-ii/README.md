# String Functions - II  - Python

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string  **S**, the task is to determine whether the string starts and ends with the characters  **'gfg'**  (case insensitive). In order to complete this task, you need to utilize the string functions  **S.lower(), S.upper(), S.startswith('string2'),**  and  **S.endswith('string2')**. By using these functions, you can check if the given string  **S**  meets the specified conditions of starting and ending with  **'gfg'**.

 **Example 1:** 

```
Input:
S: "gFgabcdEGfG"
Output:
Yes
Explanation:
The given string "gFgabcdEGfG" starts with "gfg" and also ends with "gfg" after converting it to lowercase ("gfgabcdegfg"), so the output is Yes.
```

 **Example 2:** 

```
Input:
S: "GgfhTnagfg"
Output:
No
Explanation:
The given string "GgfhTnagfg" only ends with "gfg" after converting it to lowercase ("ggfhtnagfg"), but it does not start with "gfg", so the output is No.
```

 **Your Task:** 
You are given a string, ' **S** '. You need to write a function called ' **gfg** ' that takes ' **S** ' as input and checks if the string starts and ends with the substring 'gfg'.

If the given string starts and ends with 'gfg', the function should print "Yes". Otherwise, it should print "No".

 **Constraints:** 
1 ≤ |S| ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-08T10:59:07.239Z  

```py
# Function to check if string
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    if (b.startswith('gfg') and b.endswith('gfg')):
        print("Yes")
    else:
        print("No")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/string-functions-ii/1)