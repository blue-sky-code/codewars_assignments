def array_diff(a, b):
    d=[]
    for i in a:
        if i not in b:
            d.append(i)
    # for i in range(len(a)):
        
    #         for j in range(len(b)):
    #                if a[i]!=b[j] and len(b)!=0:
    #                     d.append(a[i])
    #                else:
    #                      return(a)

    #         #for j in rangb:
                

    #         # for j in range(len(b)):

    # return d
    return d
    
    
    
print(array_diff([], [1,2]))