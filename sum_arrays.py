def sum_array(a):
    s=0
    
    for i in range(len(a)):
        if len(a)==0:
            return 0
        else:
            s=s+a[i]
    
    return(s)

print(sum_array([-2.398]))