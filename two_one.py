def longest(a1,a2):
    
    # your code
    m=[]
    n=[]
    for i in range(len(a1)):
      #print(a1[i])
      m.append(a1[i])
    
    for j in range(len(a2)):
       n.append(a2[j])
    z=m+n
    

    return "".join(sorted(list(set(z))))
   

print(longest("abcdefghijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz"))