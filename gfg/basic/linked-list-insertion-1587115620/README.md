# Linked List End Insertion

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

You are given the  **head** of a Singly Linked List and a value  **x**, insert that value  **x** at the end of the LinkedList and return the  **head** of the modified Linked List.

 **Examples :** 

```
Input: x = 6,
   
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Explanation: We can see that 6 is inserted at the end of the linkedlist.
   

```

```
Input: x = 1,
   
Output: 4 -> 5 -> 1
Explanation: We can see that 1 is inserted at the end of the linked list.
      

```

 **Constraints:** 
0 ≤ number of nodes ≤ 105
0 ≤ node->data, x ≤ 103

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T09:51:10.381Z  

```py
'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        if not head:
            head = Node(x)
            return head
        temp = head
        while temp.next:
            temp = temp.next
            
        temp.next=Node(x)
        
        return head
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1)