def grow(arr):
    s=1
    for i in range(len(arr)):
        s=s*arr[i]
        
        #print(i)
    return s

print(grow([2, 2, 2, 2, 2, 2]))

