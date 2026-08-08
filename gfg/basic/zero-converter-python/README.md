# Zero Converter - Python

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

You are given a  **number n**. The number n can be negative or positive. If n is negative, print numbers from  **n to 0**  by adding 1 to n in the  **neg**  function. If positive, print numbers from  **n-1 to 0**  by subtracting 1 from n in the  **pos**  function.

 **Note** :- You don't have to return anything, you just have to print the array.

 **Example 1:** 

```
Input:
n = 0
Output:
already Zero

```

 **Example 2:** 

```
Input:
n = 4
Output:
3 2 1 0

```

 **Example 3:** 

```
Input:
n = -3
Output:
-3 -2 -1 0
```

 **Your Task:** 
This is a function problem. You don't need to take input of test cases. Just complete the functions  **pos() and neg().** 

 **Constraints** :
-103 <= x <= 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-08T10:41:17.736Z  

```py
def pos(n):
    ## Write the code
    arr = []
    for i in range(n-1,-1,-1):
        arr.append(i)
    
    for num in arr:
        print(num,end=' ')
    
def neg(n):
    ##Write the code
    arr = []
    for i in range(n,1,1):
        arr.append(i)
        
    for num in arr:
        print(num,end=' ')
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/zero-converter-python/1)