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