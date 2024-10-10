array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def NormalSearch(n):
    i = 0
    
    while i < len(array):
        if array[i] == n:
            return i
            i = 0
        else:
            i += 1

def BinarySearch(n):
    LeftSide = 0
    RightSide = n - 1
    
    while LeftSide <= RightSide:
        MiddleNum = (LeftSide + RightSide) // 2
        
        if n == array[MiddleNum]:
            return MiddleNum
        elif n < array[MiddleNum]:
            RightSide = MiddleNum - 1
        else:
            LeftSide = MiddleNum + 1
    
    return -1
    

print(NormalSearch(4))
print(BinarySearch(4))

# Normal Search returns in a linear time
# Binary Search always divide by half; thus, the algorithm returns in log(n) time
