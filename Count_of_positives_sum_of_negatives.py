def count_positives_sum_negatives(arr):
    c=0
    s=0
    d=[]
    if len(arr)==0:
        return arr
    else:
        for i in range(len(arr)):
            if arr[i]>0:
                c=c+1
            
            elif arr[i]<0:
                s=s+arr[i]
        
    d.append(c)
    d.append(s)
        
    return(d)



print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))