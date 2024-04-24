def dig_pow(n,p):
    # if n<=10:
    #     print(n)
    # else:
    #     dig_pow(n//10)
    #     print(n%10)
    str_n= str(n)
    d=list(str_n)
    s=0
    m=[]
    for i in d:
        m.append(i)
    #print(m)
    for j in range(len(m)):
        s=s+(int(m[j])**p)
        #print(m[j])
        p=p+1
    if s==n:
        return 1
    elif s%n==0:
        return s//n
    return -1
        
        

print(dig_pow(8,3))

        

    
        
    
        
        
        
        
       

    
    
    



(dig_pow(89,1))