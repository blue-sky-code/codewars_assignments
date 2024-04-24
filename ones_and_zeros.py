def binary_array_to_number(arr):
    m=[]
    s=0
    for i in range(len(arr)):
        
        m.append(str(arr[i]))
        
        
        #s=s+m[i]*(2**(len(m)-1))
        #(len(m)-2)
        #print (s)
    a="".join(m)
    b=int(a,2)
        
    return b
    
print(binary_array_to_number([0,0,1,0]))