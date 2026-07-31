# Remove Duplicates Sorted Array

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a  **sorted array arr[]**  containing positive integers. Your task is to  **remove all duplicate elements**  from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.
 **Examples :** 

```
Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: After removing all the duplicates only one instance of 2 will remain i.e. [2] so modified array will contains 2 at first position and you should return array containing [2] after modifying the array.

```

```
Input: arr[] = [1, 2, 4]
Output: [1, 2, 4]
Explation:  As the array does not contain any duplicates so you should return [1, 2, 4].
```

 **Constraints:** 
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T11:11:35.312Z  

```py
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        i = 0
        j = 0
        result = []
        
        while (j<len(arr)):
            if arr[i]!=arr[j]:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
                
            j+=1
        for j in range(i+1):
            result.append(arr[j])
        return result
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1)