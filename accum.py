def accum(s):
    m=[]
    for i in range((len(s))):
        m.append(s[i]*(i+1))
        c="-".join(m)
        x=c.title()
    return x
        
        


        
    
    

print(accum("MjtkuBovqrU"))